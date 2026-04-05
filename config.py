import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#
# ---------------------------------------------------------
#  Microsoft Graph / Outlook / SharePoint / Teams Settings
# ---------------------------------------------------------
#

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
GRAPH_SCOPE = "https://graph.microsoft.com/.default"

#
# ---------------------------------------------------------
#  Snowflake Settings
# ---------------------------------------------------------
#

SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")

#
# ---------------------------------------------------------
#  LLM Provider Settings (NEW)
# ---------------------------------------------------------
#
LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")  
# options: openai, azure_openai, anthropic, etc.

LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")  
# default model, override in .env

LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")  
# optional: used for Azure OpenAI or custom inference servers

#
# ---------------------------------------------------------
#  Server Settings
# ---------------------------------------------------------
#

SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("SERVER_PORT", "8000"))

#
# ---------------------------------------------------------
#  Validation
# ---------------------------------------------------------
#

def validate_config():
    missing = []

    required_vars = [
        "TENANT_ID",
        "CLIENT_ID",
        "CLIENT_SECRET",
        "SNOWFLAKE_ACCOUNT",
        "SNOWFLAKE_USER",
        "SNOWFLAKE_PASSWORD",
        "SNOWFLAKE_WAREHOUSE",
        "SNOWFLAKE_DATABASE",
        "SNOWFLAKE_SCHEMA",
        "LLM_API_KEY",
    ]

    for var in required_vars:
        if globals().get(var) in (None, "", " "):
            missing.append(var)

    if missing:
        raise RuntimeError(
            f"Missing required environment variables: {', '.join(missing)}"
        )