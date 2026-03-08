import requests
import dotenv
import os
import time
import json
import traceback
from datetime import datetime

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
OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER")

def fetch_batch(batch):
    query_parts = []
    for i, user in enumerate(batch):
        query_parts.append(f"""
        u{i}: user(login: "{user}") {{
            login
            followers {{ totalCount }}
            repos: repositories(ownerAffiliations: [OWNER, COLLABORATOR], first: 100) {{
                totalCount
                repoData: nodes {{
                    name
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
    print(f"""
--- Options ---
BATCH_SIZE: {BATCH_SIZE}
OUTPUT_FOLDER: {OUTPUT_FOLDER}
""")

    results = []

    for i in range(0, len(USERNAMES), BATCH_SIZE):
        batch = USERNAMES[i:i+BATCH_SIZE]
        print(f"Fetching batch from {i} to {i+BATCH_SIZE-1}")

        try:
            data = fetch_batch(batch)
            users_data = data.get('data', {})

            for key, val in users_data.items():
                if val:
                    total_stars = 0
                    if val['repos']['repoData']:
                        total_stars += sum(repo['stargazerCount'] for repo in val['repos']['repoData'])

                    results.append({
                        "username": val['login'],
                        "stars": total_stars,
                        "followers": val['followers']['totalCount'],
                        "repos": val['repos']['totalCount'],
                        "prs": val['pullRequests']['totalCount'],
                        "commits": val['contributionsCollection']['totalCommitContributions']
                    })

        except Exception:
            print(f"An exception occurred while processing the batch:\n{traceback.format_exc()}")

        time.sleep(1)

    with open(os.path.join(OUTPUT_FOLDER, "userdata.json"), "w") as f:
        json.dump(results, f, indent=4)
    
    with open(os.path.join(OUTPUT_FOLDER, "fetchdata.json"), "w") as f:
        json.dump({
            "date": datetime.now().strftime("%B %d, %Y"),
            "user_count": len(results),
        }
        , f, indent=4)
    
    print(f"Done! Saved data for {len(results)} users to {OUTPUT_FOLDER}")
