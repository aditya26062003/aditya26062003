import requests
import json

def fetch_codeforces_stats(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["result"][0]
    else:
        return None

def update_readme(stats):
    with open("README.md", "r") as file:
        readme_content = file.readlines()

    for i, line in enumerate(readme_content):
        if line.startswith("## Codeforces Stats"):
            readme_content = readme_content[:i+1]
            break

    readme_content.append(f"Username: {stats['handle']}\n")
    readme_content.append(f"Rating: {stats['rating']}\n")
    readme_content.append(f"Rank: {stats['rank']}\n")
    readme_content.append(f"Max Rating: {stats['maxRating']}\n")
    readme_content.append(f"Max Rank: {stats['maxRank']}\n")

    with open("README.md", "w") as file:
        file.writelines(readme_content)

if __name__ == "__main__":
    import os
    handle = os.getenv("CF_HANDLE")
    stats = fetch_codeforces_stats(handle)
    if stats:
        update_readme(stats)
