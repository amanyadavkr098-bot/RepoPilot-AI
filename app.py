import streamlit as st
from github_fetcher import (
    get_folder_structure,
    get_readme,
    get_repo_contents
)
from ai_explainer import (
    summarize_readme,
    explain_folders,
    contribution_path
)
from repo_analyzer import detect_tech_stack

st.set_page_config(page_title="RepoPilot AI")

st.title("🚀 RepoPilot AI")
st.subheader("GitHub Repository Explainer for Beginners")

repo_url = st.text_input(
    "Paste GitHub Repository URL"
)

if st.button("Analyze Repository"):
    if not repo_url.strip():
        st.warning(
            "Please enter a GitHub repository URL."
        )
        st.stop()

    try:
        parts = repo_url.strip("/").split("/")

        owner = parts[-2]
        repo = parts[-1]

        with st.spinner("Fetching repository..."):

            readme = get_readme(owner, repo)

            repo_contents = get_repo_contents(
                owner,
                repo
            )

            tech_stack = detect_tech_stack(
                repo_contents
            )

            folders = get_folder_structure(
                owner,
                repo
            )

        with st.spinner("Analyzing repository with AI..."):

            summary = summarize_readme(
                readme
            )

            folder_explanation = explain_folders(
                folders
            )

            contribution_guide = contribution_path(
                summary,
                tech_stack,
                folders
            )

        st.subheader("📌 Repository Summary")
        st.markdown(summary)

        st.subheader("🛠 Tech Stack")

        for tech in tech_stack:
            st.write(f"✅ {tech}")

        st.subheader("📂 Folder Structure")
        st.markdown(folder_explanation)

        st.subheader("🚀 Contribution Path")
        st.markdown(contribution_guide)

    except Exception as e:
        st.error(f"Error: {e}")
    