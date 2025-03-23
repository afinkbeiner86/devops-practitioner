"""
EXERCISE 10: Working with REST APIs
Write a program that:

connects to GitHub API
gets all the public repositories for a specific GitHub user
prints the name & URL of every project
"""

import requests

gitlab_repo_url = "https://gitlab.com/api/v4/users/jimsemara/projects"

git_projects_respones = requests.get(gitlab_repo_url)

my_projects = git_projects_respones.json()

for project in my_projects:
    project_name = project.get("name")
    project_url = project.get("web_url")
    print(f"Project Name: {project_name}\nProject URL: {project_url}\n---")