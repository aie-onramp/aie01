# 🚀 Breakout Room #1: Build & Deploy Your First Backend – *Hot Mess Coach*

Welcome! In this breakout room we switch from frontend to backend—students will build a **Python FastAPI application**, integrate **LLM-powered chat**, analyze documents (PDF, CSV), and deploy the full backend to **Vercel**.

---

## 📚 Table of Contents

- [What Is This Demo?](#what-is-this-demo)
- [Prerequisites](#prerequisites)
- [Breakout Room #1](#breakout-room-1)
- [Step 1: Add GitFlow + Cursor Rules](#step-1-add-gitflow--cursor-rules)
- [Step 2: Create Your FastAPI "Hot Mess Coach" App](#step-2-create-your-fastapi-hot-mess-coach-app)
- [Step 3: Deploy FastAPI Backend to Vercel](#step-3-deploy-fastapi-backend-to-vercel)
- [Activity #1](#activity-1)

---

## Prerequisites

- Python 3.10+
- Cursor IDE
- GitHub account
- Vercel account
- Install Vercel CLI:
  ```bash
  npm install -g vercel
  ```

---

## 🤝 Breakout Room #1

A full hands-on backend session using FastAPI + LLM + document analysis + deployment.

---

# What Is This Demo?

Students will:

- Build a FastAPI backend
- Use Cursor agents with GitFlow rules
- Deploy to Vercel
- Add LLM chat
- Add PDF/CSV document analysis
- Learn context engineering
- Learn chunking + JSON structuring
- Test locally + redeploy

---

# 📝 Step 1: Add GitFlow + Cursor Rules

Add:

- `gitflow_rules.md`
- `cursor_rules.md`

---
# 🐍 Step 2: Create Your FastAPI "Hot Mess Coach" App

```bash

# create Github folder and clone it
git clone {ssh_keys_to_your_hot_mess_coach_repo}

# open your cloned folder
cd hot-mess-coach

# create and move to your backend folder
mkdir api
cd api

# Copy your files first
cp ../../sample_backend_scripts/STEP1_app_llm.py .
mv STEP1_app_llm.py index.py

# Move to your hot-mess-coach folder
cd ../

# Upload remaining files for the application
cp ../AIM-hot-mess-coach/requirements.txt .
cp ../AIM-hot-mess-coach/pyproject.toml .

# Add file for Vercel deployment
cp ../AIM-hot-mess-coach/vercel.json .

# Create the .venv from your pyproject
uv sync
```

Run locally:
```bash
uv run uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

Visit:

- http://localhost:8000  
- http://localhost:8000/docs 

---
# ☁️ Step 3: Deploy FastAPI Backend to Vercel

Add changes to github:
```bash
git add .
git commit -m 'adding files'
git push origin main
```

Deploy:

```bash
vercel --prod
```

Make sure to upload your OPENAI_API_KEY as environment variable in Vercel!
---

# 🏗️ Activity #1

Now it's your turn to experiment and get creative! Use this time to practice what you've learned and explore the tools.

**Experiment with Backend Customization:**

- Create your own repository
- Create .py file containing your FastAPI application
- use .env for API-KEY
- Implement extra features
- Open and merge pull requests following GitFlow best practices
- Deploy your updated backend to Vercel
---

Enjoy building your backend AI app! 🎉
