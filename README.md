# 🚀 RepoPilot AI

**RepoPilot AI** helps developers understand unfamiliar GitHub repositories faster.

Paste any GitHub repository URL and instantly get:

* 🤖 **AI-powered repository summary**
* 🛠 **Accurate tech stack breakdown**
* 📊 **Repository health metrics**
* 🚌 **Bus factor risk analysis**
* 💬 **Maintainer responsiveness insights**
* 🐛 **Beginner-friendly contribution paths**
* 📂 **Repository folder explanations**
* 🔥 **Maintainer activity heatmap**

Built for **students, open-source beginners, contributors, and developers** exploring unfamiliar codebases.

---

## ✨ Features

### 🤖 AI Repository Summary

Get a beginner-friendly explanation of what the repository does, who should contribute, and how to get started.

### 📊 Repository Health Metrics

Understand repository quality using practical engineering metrics:

* **Bus Factor Risk** — How dependent the project is on key contributors
* **Issue Closing Time** — Average time taken to close issues
* **Maintainer Responsiveness** — How active maintainers are
* **Stale Issue Detection** — Tracks inactive issues
* **Overall Health Score** — Repository quality score out of 100

### 🛠 Accurate Tech Stack Detection

Uses the **GitHub Languages API** for real language percentages instead of guessing.

Example:

```text
JavaScript — 82%
TypeScript — 12%
CSS — 4%
```

### 🧑‍💻 Beginner Contribution Guide

RepoPilot AI suggests:

* Files beginners should explore
* Good starting folders
* Beginner-friendly issue areas
* What to avoid when contributing

### 📂 Folder Explanations

Explains repository structure in a beginner-friendly way.

Example:

```text
src/ → core application logic
docs/ → documentation
tests/ → testing files
```

### 🔥 Maintainer Activity Heatmap

Shows when maintainers are most active to help contributors choose the best time to:

* Open issues
* Submit pull requests
* Ask questions

---

## 🖼 Demo

Paste any GitHub repository URL:

```text
https://github.com/facebook/react
```

RepoPilot AI instantly analyzes:

✅ Repository complexity
✅ Contribution difficulty
✅ Tech stack
✅ Maintainer activity
✅ Beginner-friendly contribution areas
✅ Repository health metrics

**Example repositories to try:**

* https://github.com/facebook/react
* https://github.com/microsoft/vscode
* https://github.com/openai/openai-python
* https://github.com/tensorflow/tensorflow
* https://github.com/pallets/flask

---

## 🏗 Architecture

```text
Frontend (FastAPI + Vanilla JS)
            ↓
        FastAPI Backend
            ↓
      GitHub REST API
            ↓
      Analysis Engine
 ├── github_fetcher.py
 ├── repo_analyzer.py
 ├── metrics_analyzer.py
 └── ai_explainer.py
            ↓
       OpenRouter LLM
            ↓
       Dashboard UI
```

---

## 📁 Project Structure

```text
RepoPilot-AI-Web/
├── main.py                    # FastAPI app
├── github_fetcher.py          # GitHub REST API client
├── repo_analyzer.py           # Tech stack & contribution analysis
├── metrics_analyzer.py        # Repository health scoring
├── ai_explainer.py            # AI-powered explanations
│
├── templates/
│   └── index.html             # Main UI
│
├── static/
│   ├── css/
│   │   └── style.css          # UI styling
│   └── js/
│       └── app.js             # Frontend logic
│
├── requirements.txt
└── .env.example
```

---

## ⚙️ Setup

Clone the repository:

```bash
git clone <your-repo-url>
cd RepoPilot-AI-Web
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment variables:

```bash
cp .env.example .env
```

Add your keys to `.env`:

```env
GITHUB_TOKEN=your_github_token
OPENROUTER_API_KEY=your_openrouter_key
```

### Required API Keys

#### GitHub Token

Used for GitHub API access and higher rate limits.

Without token:

```text
60 requests/hour
```

With token:

```text
5000 requests/hour
```

Generate token:

**GitHub → Settings → Developer Settings → Personal Access Tokens**

Minimal permissions needed:

* Public repositories
* Read-only access

#### OpenRouter API Key

Used for AI-powered repository explanations.

Get one at:

https://openrouter.ai/

---

## ▶️ Run Locally

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open in browser:

```text
http://localhost:8000
```

---

## 🔌 API Endpoint

### Analyze Repository

```http
GET /api/analyze?repo_url=<github-url-or-owner/repo>
```

### Example

```http
GET /api/analyze?repo_url=https://github.com/facebook/react
```

Returns:

* Repository summary
* Health metrics
* Tech stack
* Beginner contribution guide
* Folder explanations
* Maintainer activity
* Contribution roadmap

---

## 🧠 Tech Stack

### Backend

* FastAPI
* Python
* GitHub REST API
* OpenRouter API

### Frontend

* HTML
* CSS
* Vanilla JavaScript

### Visualization

* Plotly

---

## 🎯 Why RepoPilot AI?

Open-source repositories can be intimidating.

New contributors often struggle to understand:

* What the project does
* Where to start contributing
* Which files matter
* How active maintainers are
* Whether the repository is healthy

**RepoPilot AI solves this by turning complex repositories into beginner-friendly insights instantly.**

---

## 🚀 Future Improvements

* PR recommendation engine
* Contributor trend analysis
* Better beginner issue ranking
* Multi-repository comparison
* Repository health history tracking
* Smart issue recommendations

---

## 🤝 Contributing

Contributions are welcome.

Feel free to:

* Open issues
* Suggest improvements
* Submit pull requests

---

## 📜 License

MIT License

---

### ⭐ If you found RepoPilot AI useful, consider starring the repository!
