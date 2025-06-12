# 🚀 Python Project Setup with `uv`

This guide walks you through setting up a modern Python project using [`uv`](https://github.com/astral-sh/uv), a fast Python package manager and environment tool.

---

## Step 1: install uv
For Windows users, open **Git Bash** and run the following command to install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
This downloads and installs the latest version of uv from Astral.

---
## Step 2: install python 3.12
Use uv to install Python 3.12:
```bash
uv python install 3.12
```
This ensures your project uses a specific and up-to-date version of Python.

---

## Step 3: create venv
Set up a virtual environment in your project directory:
```bash
uv venv
```
This creates a .venv folder to isolate your dependencies.

---
## Step 4: init project
Initialize the project with configuration files (pyproject.toml, etc.):
```bash
uv init
```
This sets up a modern Python project layout with dependency management.

---
## Step 5: activate virtual environment
```bash
source .venv/Scripts/activate
```
💡 On macOS/Linux, the path may be 
```bash 
.venv/bin/activate.
```

---
## Step 6: install dependency
Install a package (e.g., FastAPI with standard extras):
```bash
uv add "fastapi[standard]"
```
This updates your pyproject.toml and installs the package in the virtual environment.

---
## Step 7: remove dependency
Remove a package if you no longer need it:
```bash
uv remove "fastapi[standard]"
```
This will uninstall the package and clean up the project configuration.

---
## Step 8: deactivate
When you're done, deactivate the virtual environment:
```bash
deactivate
```
This restores your terminal to the global Python environment.