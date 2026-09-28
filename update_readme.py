import requests
import re
from datetime import datetime

USERNAME = "almuzahidseyam"
API_URL = f"https://api.github.com/users/{USERNAME}/repos?sort=updated&direction=desc"

def get_latest_repos():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        repos = response.json()
        
        # Filter out forks and profile repo, get top 5
        recent_repos = [r for r in repos if not r['fork'] and r['name'] != USERNAME][:5]
        
        markdown = "<!-- LATEST_REPOS_START -->\n"
        markdown += "| ?? Project | ? Stars | ?? Last Updated |\n"
        markdown += "|:-----------|:---------|:----------------|\n"
        
        for repo in recent_repos:
            name = repo['name']
            url = repo['html_url']
            stars = repo['stargazers_count']
            
            # Format date beautifully
            updated_at = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
            date_str = updated_at.strftime("%b %d, %Y")
            
            markdown += f"| [{name}]({url}) | {stars} ? | {date_str} |\n"
            
        markdown += "<!-- LATEST_REPOS_END -->"
        return markdown
    except Exception as e:
        print(f"Error fetching repos: {e}")
        return None

def update_readme():
    repos_markdown = get_latest_repos()
    if not repos_markdown:
        return
        
    with open("README.md", "r", encoding="utf-8") as file:
        readme_content = file.read()

    # Replace the content between the tags
    pattern = r"<!-- LATEST_REPOS_START -->.*?<!-- LATEST_REPOS_END -->"
    
    if re.search(pattern, readme_content, re.DOTALL):
        updated_content = re.sub(pattern, repos_markdown, readme_content, flags=re.DOTALL)
    else:
        # If tags don't exist, append to the end of the file
        updated_content = readme_content + "\n\n## ?? Recently Updated Projects\n" + repos_markdown + "\n"

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(updated_content)
        print("README.md updated successfully!")

if __name__ == "__main__":
    update_readme()
