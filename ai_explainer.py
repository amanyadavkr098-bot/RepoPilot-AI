from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def summarize_readme(readme_text):
    prompt = f"""
You are RepoPilot AI.

Explain this GitHub repository for beginners.

Give output in this EXACT format:

## What This Repo Does
(short explanation)

## Main Technologies
(bullet points)

## Beginner Level
(Beginner / Intermediate / Advanced)

## Who Should Contribute
(short explanation)

## Contribution Advice
(Where beginners should start)

## Simple Explanation
(explain like a beginner)

Keep answers concise and practical.

README:
{readme_text[:4000]}
"""

    response = client.chat.completions.create(
    model="google/gemma-4-31b-it:free",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

    return response.choices[0].message.content


def explain_folders(folder_list):

    try:
        prompt = f"""
        Explain these repository folders
        for beginner contributors.

        ONLY explain important folders.

        Keep answers short.

        Format:

        folder → purpose

        Repository structure:
        {folder_list}
        """

        response = client.chat.completions.create(
            model="google/gemma-3-4b-it:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        if response and response.choices:

            message = response.choices[0].message

            if message and message.content:
                return message.content

        return "Could not explain folders."

    except Exception as e:
        return f"Folder explanation unavailable."

def contribution_path(
    summary,
    tech_stack,
    folders
):

    try:
        prompt = f"""
        You are a GitHub open-source mentor.

        Based on this repository info,
        give beginner-friendly contribution advice.

        Tell:
        1. Difficulty level
        2. Best place to start
        3. What folders to explore
        4. What to avoid
        5. Small first contribution ideas

        Keep it concise.

        Repository summary:
        {summary}

        Tech stack:
        {tech_stack}

        Folder structure:
        {folders}
        """

        response = client.chat.completions.create(
            model="google/gemma-3-4b-it:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        if response and response.choices:

            message = response.choices[0].message

            if message and message.content:
                return message.content

        return "Could not generate contribution guide."

    except Exception:
        return "Contribution guide unavailable."