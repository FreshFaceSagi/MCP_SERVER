import requests
from auth.graph_auth import graph_headers

GRAPH_BASE = "https://graph.microsoft.com/v1.0"

def list_sharepoint_files(site_id, drive_id="root"):
    url = f"{GRAPH_BASE}/sites/{site_id}/drive/{drive_id}/children"
    resp = requests.get(url, headers=graph_headers())
    resp.raise_for_status()
    data = resp.json()
    return [
        {
            "id": item["id"],
            "name": item["name"],
            "webUrl": item.get("webUrl"),
            "folder": "folder" in item,
            "file": "file" in item
        }
        for item in data.get("value", [])
    ]