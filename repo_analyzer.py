def detect_tech_stack(repo_contents):

    technologies = []

    file_names = [
        item["name"].lower()
        for item in repo_contents
    ]

    if "package.json" in file_names:
        technologies.append("Node.js / JavaScript")

    if "requirements.txt" in file_names:
        technologies.append("Python")

    if "dockerfile" in file_names:
        technologies.append("Docker")

    if "tsconfig.json" in file_names:
        technologies.append("TypeScript")

    if ".github" in file_names:
        technologies.append("GitHub Actions")

    return technologies