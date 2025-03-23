import requests

git_projects_respones = requests.get("https://gitlab.com/api/v4/users/jimsemara/projects")

my_projects = git_projects_respones.json()

for project in my_projects:
    project_name = project['name']
    project_url = project['web_url']
    print(f"---\nProject Name: {project_name}\nProject URL: {project_url}")