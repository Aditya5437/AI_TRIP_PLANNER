# ✈️ AI Trip Planner 

An end-to-end production-style LLMOps project that uses **LangGraph-based AI agent orchestration**, an **MCP-inspired modular tool architecture**, **FastAPI backend APIs**, and a **Streamlit frontend UI** for intelligent travel planning.

The application is fully **Dockerized** and deployed publicly using **Render**.

---

# 🚀 Features

- 🌍 AI-powered trip planning
- 🧠 LangGraph-based agent workflow
- 🔧 MCP-inspired tool execution architecture
- 🏨 Hotel recommendations
- 🌦️ Weather information
- 📍 Tourist place suggestions
- 💰 Budget estimation
- 🗓️ Travel itinerary generation
- ⚡ FastAPI backend APIs
- 🎨 Streamlit frontend UI
- 🐳 Dockerized multi-service architecture
- ☁️ Public cloud deployment using Render

---

# 🧠 Tech Stack

## LLM & Agent Frameworks
- LangChain
- LangGraph
- Groq LLM (`llama-3.1-8b-instant`)

## Backend
- FastAPI
- Uvicorn
- Pydantic

## Frontend
- Streamlit

## DevOps & LLMOps
- Docker
- Docker Compose
- Render Deployment

## Python Utilities
- Requests
- Python Dotenv
- Logging
- Exception Handling

---

# 🏗️ Project Architecture

```text
User
   ↓
Streamlit Frontend
   ↓
FastAPI Backend
   ↓
LangGraph Agent Workflow
   ↓
MCP Server
   ↓
Tool Registry
   ↓
Travel Planning Tools
```

---

# 📂 Project Structure

```text
AI_TRIP_PLANNER/
│
├── trip_planner/
│   ├── agent/
│   ├── config/
│   ├── exception/
│   ├── logger/
│   ├── mcp_server/
│   ├── prompt_library/
│   ├── tools/
│   └── utils/
│
├── app.py
├── streamlit_app.py
├── Dockerfile.fastapi
├── Dockerfile.streamlit
├── docker-compose.yaml
├── requirements.txt
├── setup.py
├── pyproject.toml
└── README.md
```

---

# ⚙️ Local Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_TRIP_PLANNER.git
```

```bash
cd AI_TRIP_PLANNER
```

---

## 2️⃣ Create Virtual Environment

### Windows PowerShell

```powershell
python -m venv venv
```

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run FastAPI Backend

```bash
uvicorn app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# 🐳 Docker Setup

## Build Containers

```bash
docker compose build
```

## Start Services

```bash
docker compose up
```

---

# ☁️ Deployment

The project is deployed publicly using **Render**.

## Deployment Architecture

```text
Render Service 1:
FastAPI Backend

Render Service 2:
Streamlit Frontend
```

---

# 📸 Sample Queries

- `weather in goa`
- `suggest places to visit in paris`
- `prepare a 2 day itinerary for manali`
- `budget trip plan for dubai`

---

# 🧩 MCP-Inspired Tool Architecture

The project uses a centralized MCP-style server for:
- tool registration
- tool execution
- modular orchestration
- scalable agent-tool communication

This avoids hardcoded tool execution logic and improves extensibility.

---

# 📌 Future Improvements

- Vector Database Integration
- RAG-based travel recommendations
- Conversational memory
- Real-time APIs
- LangSmith tracing
- Kubernetes deployment
- CI/CD pipelines
- Multi-agent workflows

---

# 👨‍💻 Author

Aditya Bapat

---

# ⭐ If you found this project useful, consider giving it a star!
