import requests
from auth.graph_auth import graph_headers

GRAPH_BASE = "https://graph.microsoft.com/v1.0"

def list_emails(top=10):
    # Dummy response for testing without calling Microsoft Graph
    return [
        {
            "id": f"dummy-id-{i}",
            "subject": f"Test Email {i}",
            "from": "sender@example.com",
            "receivedDateTime": "2024-01-01T12:00:00Z",
            "bodyPreview": f"This is a dummy preview for email {i}."
        }
        for i in range(1, top + 1)
    ]
# def list_emails(top=10):
#     url = f"{GRAPH_BASE}/me/messages?$top={top}"
#     resp = requests.get(url, headers=graph_headers())
#     resp.raise_for_status()
#     data = resp.json()
#     return [
#         {
#             "id": m["id"],
#             "subject": m.get("subject"),
#             "from": m.get("from", {}).get("emailAddress", {}).get("address"),
#             "receivedDateTime": m.get("receivedDateTime"),
#             "bodyPreview": m.get("bodyPreview")
#         }
#         for m in data.get("value", [])
#     ]