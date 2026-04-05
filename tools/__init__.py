from .outlook_tools import list_emails
from .sharepoint_tools import list_sharepoint_files
from .snowflake_tools import run_query
from .teams_tools import send_teams_message
from .github_tools import get_commits   # <-- ADD THIS

TOOLS = {
    "outlook_list_emails": {
        "fn": list_emails,
        "description": "List recent Outlook emails",
        "schema": {
            "type": "object",
            "properties": {
                "top": {"type": "integer", "default": 10},
            },
            "required": [],
        },
    },

    "sharepoint_list_files": {
        "fn": list_sharepoint_files,
        "description": "List files in a SharePoint site drive",
        "schema": {
            "type": "object",
            "properties": {
                "site_id": {"type": "string"},
                "drive_id": {"type": "string", "default": "root"},
            },
            "required": ["site_id"],
        },
    },

    "snowflake_run_query": {
        "fn": run_query,
        "description": "Run a SQL query in Snowflake",
        "schema": {
            "type": "object",
            "properties": {
                "sql": {"type": "string"},
            },
            "required": ["sql"],
        },
    },

    "teams_send_message": {
        "fn": send_teams_message,
        "description": "Send a message to a Teams channel",
        "schema": {
            "type": "object",
            "properties": {
                "team_id": {"type": "string"},
                "channel_id": {"type": "string"},
                "text": {"type": "string"},
            },
            "required": ["team_id", "channel_id", "text"],
        },
    },

    # -------------------------------
    # ⭐ NEW: GitHub Commit Tool
    # -------------------------------
    "github_get_commits": {
        "fn": get_commits,
        "description": "Fetch full commit details from a GitHub repository including author, message, timestamps, files, and diffs.",
        "schema": {
            "type": "object",
            "properties": {
                "owner": {"type": "string"},
                "repo": {"type": "string"},
                "branch": {"type": "string", "default": "main"},
                "per_page": {"type": "integer", "default": 20},
            },
            "required": ["owner", "repo"],
        },
    },
}