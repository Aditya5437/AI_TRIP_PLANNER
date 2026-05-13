import os
from pathlib import Path

project_name = "trip_planner"

list_of_files = [

    # Main Package
    f"{project_name}/__init__.py",

    # Agent
    f"{project_name}/agent/__init__.py",

    # Config
    f"{project_name}/config/__init__.py",

    # Exception
    f"{project_name}/exception/__init__.py",

    # Logger
    f"{project_name}/logger/__init__.py",

    # Utils
    f"{project_name}/utils/__init__.py",

    # Prompt Library
    f"{project_name}/prompt_library/__init__.py",

    # MCP Server
    f"{project_name}/mcp_server/__init__.py",
    f"{project_name}/mcp_server/tools/__init__.py",

    # Routes
    f"{project_name}/routes/__init__.py",

    # Notebook
    "notebook/.gitkeep",

    # Root Files
    "main.py",
    "streamlit_app.py",
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    ".env",
    ".gitignore",
    "README.md"
]

for filepath in list_of_files:

    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if not os.path.exists(filepath):

        with open(filepath, "w") as f:
            pass

        print(f"Created: {filepath}")

    else:
        print(f"Already exists: {filepath}")