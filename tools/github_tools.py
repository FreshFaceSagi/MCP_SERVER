import requests
from typing import Dict, Any

GITHUB_API = "https://api.github.com"

class GitHubTools:
    def __init__(self, token: str):
        self.token = token

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json"
        }

    def github_get_commits(self, owner: str, repo: str, branch: str = "main", per_page: int = 20) -> Dict[str, Any]:
        url = f"{GITHUB_API}/repos/{owner}/{repo}/commits"
        params = {
            "sha": branch,
            "per_page": per_page
        }

        response = requests.get(url, headers=self._headers(), params=params)
        response.raise_for_status()
        commits = response.json()

        detailed_commits = []

        for c in commits:
            sha = c["sha"]
            commit_url = f"{GITHUB_API}/repos/{owner}/{repo}/commits/{sha}"

            detail_resp = requests.get(commit_url, headers=self._headers())
            detail_resp.raise_for_status()
            detail = detail_resp.json()

            detailed_commits.append({
                "sha": sha,
                "author": detail.get("commit", {}).get("author", {}),
                "committer": detail.get("commit", {}).get("committer", {}),
                "message": detail.get("commit", {}).get("message"),
                "files": detail.get("files", []),
                "stats": detail.get("stats", {}),
                "html_url": detail.get("html_url")
            })

        return {"commits": detailed_commits}