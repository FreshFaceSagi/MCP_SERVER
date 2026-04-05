import requests
from auth.graph_auth import graph_headers

GRAPH_BASE = "https://graph.microsoft.com/v1.0"

def send_teams_message(team_id, channel_id, text):
    url = f"{GRAPH_BASE}/teams/{team_id}/channels/{channel_id}/messages"
    payload = {
        "body": {
            "contentType": "html",
            "content": text
        }
    }
    resp = requests.post(url, headers=graph_headers(), json=payload)
    resp.raise_for_status()
    return {"status": "sent", "id": resp.json().get("id")}