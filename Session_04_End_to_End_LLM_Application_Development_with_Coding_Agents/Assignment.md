# 🤝 Assignment: Finalize AIE-Challenge — Build Your End-to-End Application

## 📚 Table of Contents

- [Overview](#overview)
- [Step 1: Create Empty Repository and Set Up AIE-Challenge](#step-1-create-empty-repository-and-set-up-aie-challenge)
- [Step 2: Test Backend Locally](#step-2-test-backend-locally)
- [Step 3: Deploy Backend to Vercel](#step-3-deploy-backend-to-vercel)
- [Step 4: Create Frontend with v0](#step-4-create-frontend-with-v0)
- [Step 5: Test Frontend Locally](#step-5-test-frontend-locally)
- [Step 6: Deploy Frontend to Vercel](#step-6-deploy-frontend-to-vercel)
- [Step 7: Connect Frontend to Backend](#step-7-connect-frontend-to-backend)
- [Step 8: Test End-to-End Application](#step-8-test-end-to-end-application)
- [🏗️ Activity: Your Full-Stack Hot Mess Coach](#activity-your-full-stack-hot-mess-coach)
- [🎓 Tips for Success](#tips-for-success)

---

# Overview

In this assignment, you will finalize the AIE-challenge by creating a complete end-to-end application deployed on Vercel. You'll:

1. **Set up your repository** with the AIE-challenge codebase
2. **Test the backend locally** to ensure it works correctly
3. **Deploy the backend to Vercel**
4. **Create a frontend using v0** with backend awareness
5. **Test the frontend locally** before deployment
6. **Deploy the frontend to Vercel**
7. **Connect the frontend to your deployed backend**
8. **Test the complete end-to-end application**

---

# Step 1: Create Empty Repository and Set Up AIE-Challenge

## 1.1 Create an Empty GitHub Repository

1. Go to GitHub and create a new empty repository (e.g., `aie-challenge-hotmess`)
2. **Do not** initialize it with a README, .gitignore, or license

## 1.2 Clone Your Empty Repository

```bash
# Clone your empty repository
git clone git@github.com:YOUR_USERNAME/aie-challenge-hotmess.git

# Navigate into the repository
cd aie-challenge-hotmess
```

## 1.3 Add AIE-Challenge as a Remote and Pull

```bash
# Add the AIE-challenge repository as a remote (replace with actual AIE-challenge repo URL)
git remote add upstream https://github.com/AI-Maker-Space/aie-challenge-hotmess.git

# Fetch the upstream repository
git fetch upstream

# Pull the main branch from upstream
git pull upstream main --allow-unrelated-histories

# If you encounter conflicts, resolve them, then:
git add .
git commit -m "Merge AIE-challenge codebase"
```

## 1.4 Push to Your Own Repository

```bash
# Push to your own repository
git push origin main
```

You should now have the AIE-challenge codebase in your repository, including:
- `aie-challenge-hotmess-backend/` - FastAPI backend
- `AIM-hot-mess-coach-frontend/` - Frontend structure (if it exists)

---

# Step 2: Test Backend Locally

## 2.1 Navigate to Backend Directory

```bash
cd aie-challenge-hotmess-backend
```

## 2.2 Set Up Python Environment

### Option A: Using uv (recommended)

```bash
# Initialize and sync dependencies
uv sync
```

### Option B: Using venv + pip

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

## 2.3 Set OpenAI API Key

```bash
# Set your OpenAI API key as an environment variable
export OPENAI_API_KEY="sk-your-api-key-here"
```

Or create a `.env` file in the backend directory:
```bash
echo "OPENAI_API_KEY=sk-your-api-key-here" > .env
```

## 2.4 Start the Backend Server

```bash
# Using uv
uv run uvicorn api.index:app --reload --host 0.0.0.0 --port 8000

# OR using venv
uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

## 2.5 Test the Backend

Open your browser and visit:
- **Health check**: http://localhost:8000
- **API documentation**: http://localhost:8000/docs

Test the chat endpoint using curl:

```bash
curl -X POST http://localhost:8000/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello, Hot Mess Coach!"}'
```

You should receive a JSON response with an AI-generated reply. If everything works, you're ready to deploy!

---

# Step 3: Deploy Backend to Vercel

## 3.1 Commit and Push Your Changes

```bash
# Make sure you're in the repository root
cd ..  # If you're in the backend directory

# Add all changes
git add .

# Commit your changes
git commit -m "Add backend configuration and test locally"

# Push to your repository
git push origin main
```

## 3.2 Deploy to Vercel

### Option A: Using Vercel CLI

```bash
# Install Vercel CLI if you haven't already
npm install -g vercel

# Navigate to backend directory
cd aie-challenge-hotmess-backend

# Deploy to Vercel
vercel --prod
```

Follow the prompts:
- Link to existing project or create new one
- Set project name (e.g., `aie-challenge-backend`)
- Confirm deployment settings

### Option B: Using Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Import your GitHub repository
4. Set the root directory to `aie-challenge-hotmess-backend`
5. Configure build settings (Vercel should auto-detect FastAPI)
6. Add environment variable: `OPENAI_API_KEY` with your API key
7. Deploy!

## 3.3 Verify Backend Deployment

Once deployed, test your backend:

```bash
# Replace YOUR_BACKEND_URL with your actual Vercel URL
curl -X POST https://YOUR_BACKEND_URL.vercel.app/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello from production!"}'
```

Save your backend URL - you'll need it for the frontend!

---

# Step 4: Create Frontend with v0

## 4.1 Prepare Your Backend Information

Before going to v0, make sure you have:
- Your deployed backend URL (e.g., `https://your-backend.vercel.app`)
- The API endpoint: `/api/chat`
- The request format: `POST` with body `{"message": "text"}`

## 4.2 Generate Frontend in v0

1. Go to [v0.dev](https://v0.dev)
2. Use this prompt (replace with your actual backend URL):

```
Create me a frontend called "Hot Mess Coach UI" for a Thanksgiving coaching application.

This frontend must call my backend:
POST https://YOUR_BACKEND_URL.vercel.app/api/chat

Request Body:
{
  "message": "text"
}

Response:
{
  "reply": "AI-generated response"
}

Requirements:
- Use React + Next.js + TypeScript + Tailwind CSS
- Use shadcn/ui components
- Add playful, chaotic UI elements (Thanksgiving theme)
- Implement a chat interface that displays user messages and AI replies
- Show loading states while waiting for AI responses
- Handle errors gracefully
- Make it responsive and mobile-friendly
```

3. Upload your backend code (`api/index.py`) to give v0 context about your API
4. Generate and refine the frontend until you're happy with it

## 4.3 Download the Frontend

1. Click "Download" in v0
2. Extract the downloaded zip file
3. Move the frontend folder to your repository:

```bash
# From your repository root
# The downloaded folder might be named something like "frontend" or "hot-mess-coach-ui"
# Rename it if needed and move it to the appropriate location
mv ~/Downloads/hot-mess-coach-ui AIM-hot-mess-coach-frontend/frontend-hot-mess-coach
```

Or if you prefer a different structure, organize it as needed.

---

# Step 5: Test Frontend Locally

## 5.1 Navigate to Frontend Directory

```bash
cd AIM-hot-mess-coach-frontend/frontend-hot-mess-coach
```

## 5.2 Install Dependencies

```bash
npm install
```

## 5.3 Configure Backend URL

Create a `.env.local` file:

```bash
# For local development, point to your local backend
echo "NEXT_PUBLIC_BACKEND_URL=http://localhost:8000" > .env.local
```

Or export as environment variable:

```bash
export NEXT_PUBLIC_BACKEND_URL="http://localhost:8000"
```

## 5.4 Start the Frontend Development Server

```bash
npm run dev
```

## 5.5 Test the Frontend

1. Open http://localhost:3000 in your browser
2. Make sure your **backend is running** on port 8000 (from Step 2)
3. Test the chat interface:
   - Send a message
   - Verify you receive an AI response
   - Check that the UI displays correctly
   - Test error handling (stop the backend and try sending a message)

If everything works locally, you're ready to deploy!

---

# Step 6: Deploy Frontend to Vercel

## 6.1 Update Environment Variable for Production

Before deploying, update your `.env.local` or create a production config:

```bash
# Update .env.local to use your deployed backend
echo "NEXT_PUBLIC_BACKEND_URL=https://YOUR_BACKEND_URL.vercel.app" > .env.local
```

Or you can set this in Vercel's dashboard after deployment.

## 6.2 Commit and Push Frontend Changes

```bash
# From repository root
git add .
git commit -m "Add v0-generated frontend"
git push origin main
```

## 6.3 Deploy Frontend to Vercel

### Option A: Using Vercel CLI

```bash
# Navigate to frontend directory
cd AIM-hot-mess-coach-frontend/frontend-hot-mess-coach

# Deploy to Vercel
vercel --prod
```

### Option B: Using Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Import your GitHub repository
4. Set the root directory to `AIM-hot-mess-coach-frontend/frontend-hot-mess-coach`
5. Configure build settings:
   - Framework Preset: Next.js
   - Build Command: `npm run build` (or leave default)
   - Output Directory: `.next` (or leave default)
6. Add environment variable: `NEXT_PUBLIC_BACKEND_URL` = `https://YOUR_BACKEND_URL.vercel.app`
7. Deploy!

## 6.4 Verify Frontend Deployment

Visit your deployed frontend URL and verify it loads correctly.

---

# Step 7: Connect Frontend to Backend

## 7.1 Verify Backend URL in Frontend

Make sure your frontend is configured to use your deployed backend:

1. Check Vercel environment variables for your frontend project
2. Ensure `NEXT_PUBLIC_BACKEND_URL` is set to your deployed backend URL
3. If you need to update it, go to Vercel Dashboard → Your Frontend Project → Settings → Environment Variables

## 7.2 Update Frontend Code (if needed)

If the frontend code doesn't automatically use the environment variable, you may need to update the API call. Ask Cursor AI agents to help:

```
Help me connect my frontend to my backend. The backend URL should be read from 
NEXT_PUBLIC_BACKEND_URL environment variable. The endpoint is POST /api/chat 
with body {"message": "text"}.
```

## 7.3 Redeploy Frontend (if changes were made)

```bash
# If you made code changes
git add .
git commit -m "Connect frontend to deployed backend"
git push origin main

# Vercel will automatically redeploy, or you can trigger manually
```

---

# Step 8: Test End-to-End Application

## 8.1 Test the Complete Application

1. Visit your deployed frontend URL
2. Test the chat interface:
   - Send various messages
   - Verify AI responses are received
   - Check that the UI updates correctly
   - Test on mobile if possible

## 8.2 Verify Both Services Are Working

- **Backend**: Test directly at `https://YOUR_BACKEND_URL.vercel.app/api/chat`
- **Frontend**: Test the full user experience at `https://YOUR_FRONTEND_URL.vercel.app`

## 8.3 Create README Documentation

Ask Cursor AI agents to create a comprehensive README:

```
Create a README.md file for this project with:
- Project description
- Prerequisites
- Local setup instructions for both backend and frontend
- Deployment instructions
- API documentation
- Troubleshooting tips
```

---

# 🏗️ Activity: Your Full-Stack Hot Mess Coach

## Required Tasks

- ✅ Set up repository with AIE-challenge codebase
- ✅ Test backend locally
- ✅ Deploy backend to Vercel
- ✅ Create frontend with v0
- ✅ Test frontend locally
- ✅ Deploy frontend to Vercel
- ✅ Connect frontend to backend
- ✅ Test end-to-end application

## Advanced (Optional)

- Enhance the v0-generated frontend with custom features
- Add additional backend endpoints
- Implement advanced error handling
- Add authentication or user management
- Improve UI/UX with animations and transitions

---

# 🎓 Tips for Success

- **Use Cursor AI agents** throughout the process - they can help with git commands, code fixes, and configuration
- **Test locally first** - Always verify everything works locally before deploying
- **Check environment variables** - Make sure `OPENAI_API_KEY` and `NEXT_PUBLIC_BACKEND_URL` are set correctly in Vercel
- **Give v0 clear instructions** - Include your backend URL, endpoint details, and JSON format in your prompt
- **Keep your code organized** - Use proper folder structure and commit frequently
- **Read error messages carefully** - Vercel deployment logs and browser console will help you debug issues
- **Test CORS** - If you see CORS errors, check that your backend allows the frontend origin

---

## 🎉 Congratulations!

Once you've completed all steps, you'll have a fully functional end-to-end LLM application deployed on Vercel! Your Hot Mess Coach is ready to help users navigate their Thanksgiving challenges (or any other coaching scenario you've configured).
