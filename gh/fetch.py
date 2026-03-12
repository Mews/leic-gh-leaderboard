import requests
import dotenv
import os
import time
import json
import traceback
from datetime import datetime, timezone

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
MAX_RETIRES = int(os.getenv("MAX_RETIRES"))

def fetch_batch(batch, retries=0):
    query_parts = []
    for i, user in enumerate(batch):
        query_parts.append(f"""
        u{i}: user(login: "{user}") {{
            login
            followers {{ totalCount }}
            repos: repositories(ownerAffiliations: OWNER, first: 100) {{
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
    
    # Implement the guidelines in
    # https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api?apiVersion=2022-11-28
    if response.status_code == 403:
        if retries >= 5:
            print(response.content)
            response.raise_for_status()
        
        if "retry-after" in response.headers:
            retry_after = float(response.headers.get("retry-after"))
            print(f"retry-after found\nwaiting for {retry_after} seconds")
            time.sleep(retry_after)
            return fetch_batch(batch, retries + 1)

        elif "x-ratelimit-remaining" in response.headers and str(response.headers.get("x-ratelimit-remaining")).strip() == "0":
            x_ratelimit_reset = int(response.headers.get("x-ratelimit-reset", datetime.now(timezone.utc).timestamp()))
            
            print(f"is x-ratelimit-remaining 0\nresuming after utc time {x_ratelimit_reset}")
            
            sleep_time = x_ratelimit_reset - int(datetime.now(timezone.utc).timestamp())
            sleep_time = max(0, sleep_time) + 1

            print(f"sleeping for {sleep_time} seconds")
            time.sleep(sleep_time)
            
            return fetch_batch(batch, retries + 1)

        else:
            print(f"no rate limit headers present\nretry number {retries}\nwaiting for{60 + (2**retries)}")
            time.sleep(60 + (2**retries))
            return fetch_batch(batch, retries + 1)

    response.raise_for_status()
    
    return response.json()


if __name__ == "__main__":
    print(f"""
--- Options ---
BATCH_SIZE: {BATCH_SIZE}
OUTPUT_FOLDER: {OUTPUT_FOLDER}
MAX_RETRIES: {MAX_RETIRES}
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
                    top5repos = []
                    if val['repos']['repoData']:
                        total_stars += sum(repo['stargazerCount'] for repo in val['repos']['repoData'])
                        top5repos = sorted(val['repos']['repoData'], key=lambda x:x['stargazerCount'], reverse=True)[0:5]

                    results.append({
                        "username": val['login'],
                        "stars": total_stars,
                        "followers": val['followers']['totalCount'],
                        "repos": val['repos']['totalCount'],
                        "prs": val['pullRequests']['totalCount'],
                        "commits": val['contributionsCollection']['totalCommitContributions'],
                        "top5repos": top5repos
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
