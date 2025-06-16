## Step 1: install uv
For Windows users, open **Git Bash** and run the following command to install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
This downloads and installs the latest version of uv from Astral.


## Step 2: install python 3.12
Use uv to install Python 3.12:
```bash
uv python install 3.12
```
This ensures your project uses a specific and up-to-date version of Python.



## Step 3: create venv
Set up a virtual environment in your project directory:
```bash
uv venv
```
This creates a .venv folder to isolate your dependencies.


## Step 4: init project
Initialize the project with configuration files (pyproject.toml, etc.):
```bash
uv init
```
This sets up a modern Python project layout with dependency management.


## Step 5: activate virtual environment
```bash
source .venv/Scripts/activate
```
💡 On macOS/Linux, the path may be 
```bash 
source .venv/bin/activate
```


## Step 6: install dependency
Install a package (e.g., FastAPI with standard extras):
```bash
uv add "fastapi[standard]"
```
This updates your pyproject.toml and installs the package in the virtual environment.



## Step 7: simple fastapi to main.py
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

## Step 8: Run the live server
```bash
fastapi dev main.py
```
In the output, there's a line with something like:

`INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)`

That line shows the URL where your app is being served, in your local machine.

## Check it
Open your browser at http://127.0.0.1:8000.

You will see the JSON response as:

```
{"message": "Hello World"}
```

## Interactive API docs
Now go to http://127.0.0.1:8000/docs.

You will see the automatic interactive API documentation (provided by Swagger UI):

## Alternative API docs
And now, go to http://127.0.0.1:8000/redoc.

You will see the alternative automatic documentation (provided by ReDoc):

## Operation
`Operation` here refers to one of the HTTP "methods".

One of:
- POST
- GET
- PUT
- DELETE

...and the more exotic ones:

- OPTIONS
- HEAD
- PATCH
- TRACE

In the HTTP protocol, you can communicate to each path using one (or more) of these "methods".

When building APIs, you normally use these specific HTTP methods to perform a specific action.

Normally you use:

- POST: to create data.
- GET: to read data.
- PUT: to update data.
- DELETE: to delete data.

# Recap
- Import FastAPI.
- Create an app instance.
- Write a path operation decorator using decorators like @app.get("/").
- Define a path operation function; for example, def root(): ....
- Run the development server using the command fastapi dev.

---
# Workshop 5.5 (Git) 
## Stages all changes (new, modified, or deleted files) in the current directory and all subdirectories
```bash
git add .
```
It stages all changes in your working directory 

## Creates a new commit
```bash
git commit -m “init project”
```
It creates a new commit with all currently staged changes and attaches the message "init project" to that commit.

## Configure Git identity
```bash
git config --global user.email "YOUR_EMAIL"
git config --global user.name "YOUR_USERNAME"
```
These two commands configure your global Git identity — which tells Git who you are when making commits.
### 📍 Notes:
The --global flag makes this setting apply to all repos for the current user account.

If you want to set it only for a specific repo, remove --global and run the commands inside the repo:
```bash
git config user.email "YOUR_EMAIL"
git config user.name "YOUR_USERNAME"
```

## Connects your local Git repository to a remote repository
```bash
git remote add origin YOUR_URL
```
## Uploads your local master branch
It uploads your local master branch commits to the remote repository named origin.
```bash
git push origin master
```

[Previous Workshop](../workshop_004/readme.md) | [Next Workshop](../workshop_006/readme.md)
