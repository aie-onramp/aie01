# 🤝 Assignment: Build Your Full-Stack *Hot Mess Coach* (Backend + LLM + Optional Frontend)

## 📚 Table of Contents

- [Overview](#overview)
- [Part 1 — Backend: Build FastAPI + LLM + Deploy to Vercel 🐍☁️](#part-1--backend-build-fastapi--llm--deploy-to-vercel)
  - [Step 1: Set Up Your Environment 🏗️](#step-1-set-up-your-environment-)
  - [Step 2: Scaffold Your FastAPI Backend 🧱](#step-2-scaffold-your-fastapi-backend-)
  - [Step 3: Deploy FastAPI Backend to Vercel](#step-3-deploy-fastapi-backend-to-vercel)
- [Part 2 — Advanced Build: Add Frontend to Your Backend (One-Shot Vibecoding) 🎨⚡](#part-2--advanced-build-add-frontend-to-your-backend-one-shot-vibecoding)
  - [Step 4: Choose Your Frontend (Recommended: Hot Mess Frontend) 💅](#step-4-choose-your-frontend-recommended-hot-mess-frontend-)
  - [Step 5: Generate a New Frontend in v0 with Backend Awareness 🧠→🎬](#step-5-generate-a-new-frontend-in-v0-with-backend-awareness-)
  - [Step 6: Connect Your Frontend → Backend 🔗](#step-6-connect-your-frontend--backend-)
  - [Step 7: Add to Github repo and deploy the frontend to Vercel 🌐](#step-7-add-to-github-repo-and-deploy-the-frontend-to-vercel-)
- [🏗️ Activity #1: Your Full-Stack Hot Mess Coach](#activity-1-your-full-stack-hot-mess-coach)
- [🎓 Tips for Success](#tips-for-success)

---

# Overview

In this take-home assignment, you will:

1. **Build your own Python FastAPI backend**
2. **Add an LLM endpoint** so users can talk to “Hot Mess Coach”
3. **Deploy the backend to Vercel**
4. (Advanced) **Create a frontend that calls your backend**
5. (Advanced) **Use one-shot vibecoding in v0 to generate a frontend that automatically integrates the backend**

---

# Part 1 — Backend: Build FastAPI + LLM + Deploy to Vercel 🐍☁️

---

## Step 1: Set Up Your Environment 🏗️

Add:

- `gitflow_rules.md`
- `cursor_rules.md`

---

## Step 2: Scaffold Your FastAPI Backend 🧱


```bash

# create Github folder and clone it
git clone {ssh_keys_to_your_hot_mess_coach_repo}

# open your cloned folder
cd hot-mess-coach

# create and move to your backend folder
mkdir api
cd api

# Copy your files first
cp ../../sample_backend_scripts/STEP4_app_llm.py .
mv STEP4_app_llm.py index.py

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

Run:

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

# Part 2 — Advanced Build: Add Frontend to Your Backend (One-Shot Vibecoding) 🎨⚡

---

## Step 4: Choose Your Frontend (Recommended: Hot Mess Frontend) 💅

You may reuse the *Hot Mess Tracker* frontend from class or generate a new one.

---

## Step 5: Generate a New Frontend in v0 with Backend Awareness 🧠→🎬

Example prompt:

```
Create me a frontend called “Hot Mess Coach UI”, the frontend will be used for this application {upload the backend for your application}.

This frontend must call my backend:
POST https://YOUR_BACKEND.vercel.app/chat

Body:
{ "message": "text" }

Use React + Tailwind + shadcn/ui.
Add playful chaotic UI elements.
Implement a chat interface that displays the LLM replies.
```

Download the frontend to your application folder, use 'npm install' to install dependencies, and test the frontend with 'npm run dev'.
---

## Step 6: Connect Your Frontend → Backend 🔗

Ask Cursor agents to create the connection, locally. Also ask them to create a README file with instructions how to run.

Most often, run locally backend:
```bash
uv run uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

Run locally frontend:
```bash
npm run dev
```

Open frontend (click on port 3000)
---

## Step 7: Add to Github repo and deploy the frontend to Vercel 🌐

Add changes to github:
```bash
git add .
git commit -m 'adding files'
git push origin main
```

```bash
vercel --prod
```

Make sure to add your backend url to the frontend application.
Your full-stack Hot Mess Coach is now live! 🎉

---

# 🏗️ Activity #1: Your Full-Stack Hot Mess Coach

### Required
- Build FastAPI backend   
- Deploy backend  

### Advanced
- Create frontend using v0 or reuse Hot Mess frontend  
- Connect to backend  
- Deploy frontend  

---

# 🎓 Tips for Success

- Use Cursor AI agents with your GitFlow rules  
- Test locally before deploying  
- Give v0 clear instructions (backend URL, endpoint, JSON format)  
- Keep your code clean and modular  

---
