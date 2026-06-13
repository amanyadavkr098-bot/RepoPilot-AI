import streamlit as st
import pandas as pd
import plotly.express as px

from github_fetcher import (
    get_readme,
    get_repo_contents,
    get_folder_structure,
    get_repo_issues,
    get_repo_activity,
    get_repo_languages,
    get_contributors,
    get_closed_issues
)

from ai_explainer import (
    summarize_readme,
    explain_folders,
    contribution_path
)

from repo_analyzer import (
    detect_tech_stack,
    language_contribution_score,
    beginner_contribution_areas,
    maintainer_activity_heatmap
)

from metrics_analyzer import generate_metrics_summary


st.set_page_config(
    page_title="RepoPilot AI",
    layout="wide"
)

st.title("🚀 RepoPilot AI")
st.subheader(
    "AI-powered Open Source Onboarding Assistant"
)

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

        if len(parts) < 2:
            st.error(
                "Invalid GitHub repository URL."
            )
            st.stop()

        owner, repo = parts[-2], parts[-1]

        st.info(
            f"Analyzing: {owner}/{repo}"
        )

        # -------------------
        # Fetch GitHub Data
        # -------------------
        with st.spinner(
            "Fetching repository..."
        ):

            readme = get_readme(
                owner, repo
            )

            repo_contents = (
                get_repo_contents(
                    owner, repo
                )
            )

            folders = (
                get_folder_structure(
                    owner, repo
                )
            )

            issues = get_repo_issues(
                owner, repo
            )

            comments = (
                get_repo_activity(
                    owner, repo
                )
            )

            languages_data = (
                get_repo_languages(
                    owner, repo
                )
            )

            contributors = (
                get_contributors(
                    owner, repo
                )
            )

            closed_issues = (
                get_closed_issues(
                    owner, repo
                )
            )

        # -------------------
        # Analysis
        # -------------------
        tech_stack = list(
            languages_data.keys()
        )

        total_bytes = sum(
            languages_data.values()
        )

        language_percentages = {}

        if total_bytes > 0:

            language_percentages = {
                lang: round(
                    (size / total_bytes)
                    * 100,
                    2
                )
                for lang, size
                in languages_data.items()
            }

        else:
            tech_stack = (
                detect_tech_stack(
                    repo_contents
                )
            )

            language_percentages = {
                tech: 1
                for tech
                in tech_stack
            }

        language_scores = (
            language_contribution_score(
                tech_stack
            )
        )

        beginner_areas = (
            beginner_contribution_areas(
                tech_stack
            )
        )

        heatmap_data, top_hours = (
            maintainer_activity_heatmap(
                comments
            )
        )

        metrics = (
            generate_metrics_summary(
                contributors,
                closed_issues,
                issues,
                comments,
                heatmap_data
            )
        )

        # -------------------
        # AI Calls
        # -------------------
        with st.spinner(
            "Analyzing repository..."
        ):

            try:
                summary = (
                    summarize_readme(
                        readme
                    )
                )

            except Exception:
                summary = f"""
## What This Repo Does

This repository belongs to **{owner}/{repo}**.

RepoPilot detected
**{len(tech_stack)} technologies**
and **{len(folders)} major folders**.

AI summary unavailable.

You can still explore:
- Technology stack
- Contribution paths
- Issues
- Maintainer activity
"""

            try:
                folder_explanation = (
                    explain_folders(
                        folders
                    )
                )

            except Exception:
                folder_explanation = (
                    "\n".join(
                        f"• {folder}"
                        for folder
                        in folders
                    )
                )

            try:
                contribution_guide = (
                    contribution_path(
                        summary,
                        tech_stack,
                        folders
                    )
                )

            except Exception:
                contribution_guide = """
### Beginner Roadmap

1. Read README.md  
2. Explore docs/ or examples/  
3. Search for beginner issues  
4. Avoid core architecture changes  
5. Start with small PRs
"""

        # -------------------
        # Dashboard Metrics
        # -------------------
        if "Advanced" in summary:
            difficulty, score = (
                "Advanced", 35
            )
        elif "Beginner" in summary:
            difficulty, score = (
                "Beginner", 90
            )
        else:
            difficulty, score = (
                "Intermediate", 65
            )

        col1, col2, col3, col4 = (
            st.columns(4)
        )

        col1.metric(
            "🎯 Difficulty",
            difficulty
        )

        col2.metric(
            "🛠 Technologies",
            len(tech_stack)
        )

        col3.metric(
            "📂 Folders",
            len(folders)
        )

        col4.metric(
            "🚀 Contribution Score",
            f"{score}/100"
        )

        st.progress(score / 100)

        # -------------------
        # Repository Summary
        # -------------------
        st.subheader(
            "📌 Repository Summary"
        )

        st.markdown(summary)

        # -------------------
        # Repository Health
        # -------------------
        st.subheader(
            "📊 Repository Health Metrics"
        )

        col1, col2, col3 = (
            st.columns(3)
        )

        col1.metric(
            "🚌 Bus Factor Risk",
            metrics["bus_factor"][
                "risk_level"
            ],
            f"{metrics['bus_factor']['top_contributor_share']}% top contributor"
        )

        col2.metric(
            "⏱ Issue Closing Time",
            f"{metrics['issue_closing']['avg_days']} days",
            f"{metrics['issue_closing']['rating']} "
            f"{metrics['issue_closing']['emoji']}"
        )

        col3.metric(
            "💬 Maintainer Response",
            f"{metrics['maintainer_responsiveness']['score']}/100",
            metrics[
                "maintainer_responsiveness"
            ]["rating"]
        )

        col4, col5, col6 = (
            st.columns(3)
        )

        col4.metric(
            "⚠️ Stale Issues",
            f"{metrics['stale_issues']['count']} stale",
            f"{len(issues)} open • "
            f"{metrics['stale_issues']['percentage']}% "
            f"{metrics['stale_issues']['status']}"
        )

        col5.metric(
            "💚 Overall Health",
            f"{metrics['overall_health']['score']}/100",
            f"{metrics['overall_health']['status']} "
            f"{metrics['overall_health']['emoji']}"
        )

        col6.metric(
            "👥 Contributors",
            len(contributors)
            if contributors
            else "Unknown",
            "tracked"
        )

        # -------------------
        # Technology Graph
        # -------------------
        st.subheader(
            "🛠 Technology Stack"
        )

        if tech_stack:

            tech_df = pd.DataFrame({
                "Technology":
                list(
                    language_percentages
                    .keys()
                ),

                "Percentage":
                list(
                    language_percentages
                    .values()
                ),

                "Beginner Score":
                [
                    language_scores.get(
                        lang,
                        50
                    )
                    for lang
                    in language_percentages
                ]
            })

            fig = px.bar(
                tech_df,
                x="Technology",
                y="Percentage",
                text="Percentage",
                title="Repository Language Distribution"
            )

            fig.update_traces(
                texttemplate="%{text:.1f}%",
                textposition="outside"
            )

            fig.update_layout(
                xaxis_title="Languages",
                yaxis_title="Percentage (%)",
                yaxis=dict(
                    range=[0, 100]
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # -------------------
        # Beginner Guide
        # -------------------
        st.subheader(
            "🧑‍💻 Beginner Contribution Guide"
        )

        beginner_keywords = [
            "good first issue",
            "good-first-issue",
            "bug",
            "documentation",
            "docs",
            "help wanted",
            "starter",
            "easy"
        ]

        for area in beginner_areas:

            st.markdown(
                f"### {area['language']}"
            )

            st.write(
                "📂 Focus Files:"
            )

            for file in area["files"]:
                st.write(f"• {file}")

            st.write(
                f"🎯 Focus Area: "
                f"{area['focus']}"
            )

            st.write(
                "🐛 Related Open Issues:"
            )

            shown = 0

            for issue in issues:

                labels = [
                    label["name"]
                    .lower()
                    for label in issue.get(
                        "labels",
                        []
                    )
                ]

                if any(
                    keyword in label
                    for keyword
                    in beginner_keywords
                    for label
                    in labels
                ):
                    st.markdown(
                        f"• "
                        f"[{issue.get('title','')}]"
                        f"({issue.get('html_url','')})"
                    )

                    shown += 1

                if shown >= 3:
                    break

            if shown == 0:

                st.info(
                    "No beginner-friendly "
                    "issues found.\n\n"
                    "Showing recent issues."
                )

                for issue in issues[:3]:
                    st.markdown(
                        f"• "
                        f"[{issue.get('title','')}]"
                        f"({issue.get('html_url','')})"
                    )

        # -------------------
        # Folder Structure
        # -------------------
        st.subheader(
            "📂 Folder Structure"
        )

        st.markdown(
            folder_explanation
        )

        # -------------------
        # Contribution Path
        # -------------------
        st.subheader(
            "🚀 Contribution Path"
        )

        st.markdown(
            contribution_guide
        )

        # -------------------
        # Activity Heatmap
        # -------------------
        st.subheader(
            "🔥 Maintainer Activity Heatmap"
        )

        heatmap_df = pd.DataFrame(
            heatmap_data
        )

        heatmap_fig = px.bar(
            heatmap_df,
            x="hour",
            y="activity",
            title="Maintainer Response Activity"
        )

        st.plotly_chart(
            heatmap_fig,
            use_container_width=True
        )

        st.write(
            "⏰ Best Time to Open PRs:"
        )

        for hour, count in top_hours:
            st.write(
                f"• {hour}:00 UTC "
                f"({count} interactions)"
            )

    except Exception as e:
        st.error(f"Error: {e}")