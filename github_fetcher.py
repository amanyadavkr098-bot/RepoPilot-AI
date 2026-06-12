import requests


def get_readme(owner, repo):
    """
    Fetch README from a GitHub repository
    """

    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    headers = {
        "Accept": "application/vnd.github.v3.raw"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text

    return "README not found."
def get_repo_contents(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return []
def get_folder_structure(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    response = requests.get(url)

    important_items = []

    if response.status_code == 200:

        for item in response.json():

            name = item["name"]

            if item["type"] == "dir":

                important_items.append(name)

            elif name.lower() in [
                "package.json",
                "requirements.txt",
                "dockerfile",
                "readme.md",
                "contributing.md"
            ]:
                important_items.append(name)

    return important_items