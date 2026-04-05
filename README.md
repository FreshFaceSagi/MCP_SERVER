# MCP Server — Model Context Protocol Server (Python)

## 🚀 Overview
This repository contains a production‑grade **Model Context Protocol (MCP) Server** implemented in Python.  
It exposes enterprise‑grade tools to LLMs over a secure WebSocket transport, including:

- Microsoft Graph (Outlook, Teams, SharePoint)
- Snowflake
- Custom business logic
- OAuth2 authentication
- FastAPI‑based MCP transport
- Fully typed tool schemas

The server is designed for **local development**, **enterprise deployment**, and **LLM orchestration**.

---

## 🏗️ Project Structure

mcp-server/ │ ├── server.py ├── config.py ├── requirements.txt ├── .env │ ├── tools/ │   ├── outlook_tools.py │   ├── teams_tools.py │   ├── sharepoint_tools.py │   ├── snowflake_tools.py │   └── init.py │ ├── auth/ │   ├── graph_auth.py │   ├── snowflake_auth.py │   └── init.py │ └── utils/ ├── logger.py ├── validators.py └── init.p


---

## 🔧 Installation

### 1. Clone the repository

git clone <repo-url> cd mcp-server



### 2. Install dependencies

pip install -r requirements.txt


---

## 🔐 Environment Variables

Create a `.env` file in the project root:

TENANT_ID=<your-tenant-id> CLIENT_ID=<your-app-client-id> CLIENT_SECRET=<your-client-secret>
SNOWFLAKE_USER=<username> SNOWFLAKE_PASSWORD=<password> SNOWFLAKE_ACCOUNT=<account> SNOWFLAKE_WAREHOUSE=<warehouse> SNOWFLAKE_DATABASE=<database> SNOWFLAKE_SCHEMA=<schema>



These values come from Azure App Registration and Snowflake.

---

## 🧠 Authentication

### Microsoft Graph
Uses OAuth2 Client Credentials with:

- Azure App Registration  
- Microsoft Graph SDK  

### Snowflake
Uses:

- Snowflake Python Connector  
- Username/password or key‑pair auth  

---

## ▶️ Running the MCP Server

### Start the server


uvicorn server:app --host 0.0.0.0 --port 8000 --reload


### Verify

Open:


http://localhost:8000/docs


---

## 🧩 MCP Integration

Example MCP client configuration:

```json
{
  "mcpServers": {
    "enterprise-mcp": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}

The client will:
- Connect to the MCP server
- Request tool schemas
- Invoke tools
- Receive structured JSON responses


Available Tools
|  |  | 
| outlook.send_mail |  | 
| outlook.list_messages |  | 
| teams.list_channels |  | 
| sharepoint.list_files |  | 
| snowflake.query |  | 




xample Tool Calls
Outlook Example
{
  "tool": "outlook.send_mail",
  "input": {
    "to": "user@example.com",
    "subject": "Test",
    "body": "Hello from MCP"
  }
}




{
  "tool": "outlook.send_mail",
  "input": {
    "to": "user@example.com",
    "subject": "Test",
    "body": "Hello from MCP"
  }
}

Snowflake Example
{
  "tool": "snowflake.query",
  "input": {
    "sql": "SELECT CURRENT_TIMESTAMP()"
  }
}



📦 Deployment
Docker
docker build -t mcp-server .
docker run -p 8000:8000 --env-file .env mcp-server


Cloud Options
- Azure App Service
- Azure Container Apps
- Kubernetes

📚 Logging
Centralized logging via utils/logger.py.
Levels:
- INFO — tool calls
- DEBUG — request/response bodies
- ERROR — exceptions

🧭 Troubleshooting
Missing Graph Permissions
Ensure your Azure App Registration includes:
- Mail.Read
- Mail.Send
- Files.Read.All
- Sites.Read.All
- Chat.Read
- Channel.ReadBasic.All
Snowflake Errors
Verify:
- Account identifier
- Warehouse/database/schema
- Network access rules

📝 License
Internal enterprise use unless otherwise specified.

---

If you want, I can also generate:

- a **deep‑architecture version** with diagrams  
- a **GitHub‑badged version**  
- a **multi‑file `/docs` folder**  
- or a **whitepaper‑grade README** with full flows and code  

Just tell me the direction you want to take this.


{
  "tool": "snowflake.query",
  "input": {
    "sql": "SELECT CURRENT_TIMESTAMP()"
  }
}

Deployment
Docker
docker build -t mcp-server .
docker run -p 8000:8000 --env-file .env mcp-server


Cloud Options
- Azure App Service
- Azure Container Apps
- Kubernetes

📚 Logging
Centralized logging via utils/logger.py.
Levels:
- INFO — tool calls
- DEBUG — request/response bodies
- ERROR — exceptions

🧭 Troubleshooting
Missing Graph Permissions
Ensure your Azure App Registration includes:
- Mail.Read
- Mail.Send
- Files.Read.All
- Sites.Read.All
- Chat.Read
- Channel.ReadBasic.All
Snowflake Errors
Verify:
- Account identifier
- Warehouse/database/schema
- Network access rules

📝 License
Internal enterprise use unless otherwise specified.

---

If you want, I can also generate:

- a **deep‑architecture version** with diagrams  
- a **GitHub‑badged version**  
- a **multi‑file `/docs` folder**  
- or a **whitepaper‑grade README** with full flows and code  

Just tell me the direction you want to take this.




docker build -t mcp-server .
docker run -p 8000:8000 --env-file .env mcp-server

Cloud Options
- Azure App Service
- Azure Container Apps
- Kubernetes


 Logging
Centralized logging via utils/logger.py.
Levels:
- INFO — tool calls
- DEBUG — request/response bodies
- ERROR — exceptions


Troubleshooting
Missing Graph Permissions
Ensure your Azure App Registration includes:
- Mail.Read
- Mail.Send
- Files.Read.All
- Sites.Read.All
- Chat.Read
- Channel.ReadBasic.All
Snowflake Errors
Verify:
- Account identifier
- Warehouse/database/schema
- Network access rules





