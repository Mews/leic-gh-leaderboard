import requests
import dotenv
import os
import time
import json
import traceback

dotenv.load_dotenv(".env")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
API_URL = "https://api.github.com/graphql"
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

USERNAMES = []
with open("usernames.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            USERNAMES.append(line)

BATCH_SIZE = int(os.getenv("QUERY_BATCH_SIZE"))
OUTPUT_FILE = os.getenv("DATA_SAVE_FILE")

def fetch_batch(batch):
    query_parts = []
    for i, user in enumerate(batch):
        query_parts.append(f"""
        u{i}: user(login: "{user}") {{
            login
            followers {{ totalCount }}
            ownRepos: repositories(ownerAffiliations: OWNER, first: 100) {{
                totalCount
                totalStargazers: nodes {{
                    stargazerCount
                }}
            }}
            collaboratorRepos: repositories(ownerAffiliations: COLLABORATOR, first: 100) {{
                totalCount
                totalStargazers: nodes {{
                    stargazerCount
                }}
            }}
            pullRequests {{ totalCount }}
            contributionsCollection {{
                totalCommitContributions
            }}
        }}
        """)
    
    full_query = "query { " + " ".join(query_parts) + " }"
    
    response = requests.post(API_URL, json={'query': full_query}, headers=HEADERS)
    
    response.raise_for_status()
    
    return response.json()


if __name__ == "__main__":
    results = []

    for i in range(0, len(USERNAMES), BATCH_SIZE):
        batch = USERNAMES[i:i+BATCH_SIZE]
        print(f"Fetching batch from {i} to {i+BATCH_SIZE-1}")

        try:
            data = fetch_batch(batch)
            users_data = data.get('data', {})

            with open("wow.txt", "w") as f:
                f.write(str(data))
            import sys
            sys.exit(1)

            for key, val in users_data.items():
                if val:
                    total_stars = 0
                    if val['ownRepos']['totalStargazers']:
                        total_stars = sum(repo['stargazerCount'] for repo in val['ownRepos']['totalStargazers'])
                    if val['collaboratorRepos']['totalStargazers']:
                        total_stars = sum(repo['stargazerCount'] for repo in val['collaboratorRepos']['totalStargazers'])
                        

                    results.append({
                        "username": val['login'],
                        "stars": total_stars,
                        "followers": val['followers']['totalCount'],
                        "repos": val['ownRepos']['totalCount']+val['collaboratorRepos']['totalCount'],
                        "prs": val['pullRequests']['totalCount'],
                        "commits_year": val['contributionsCollection']['totalCommitContributions']
                    })

        except Exception:
            print(f"An exception occurred while processing the batch:\n{traceback.format_exc()}")

        time.sleep(1)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=4)
    
    print(f"Done! Saved data for {len(results)} users to {OUTPUT_FILE}")
