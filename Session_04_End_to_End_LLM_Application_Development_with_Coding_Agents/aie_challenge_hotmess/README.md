<p align="center" draggable="false"><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" width="200px" height="auto"/></p>

## <h1 align="center" id="heading">🦃 Hot Mess Coach at Thanksgiving — LLM Application</h1>

An end-to-end LLM application that helps you navigate Thanksgiving challenges with style! This full-stack application features a Next.js frontend with an interactive questionnaire and chat interface, powered by a FastAPI backend that integrates with the OpenAI API to provide personalized, humorous coaching for your Thanksgiving gathering.
This application is based on the backend from the AI-Engineer-Challenge: https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge

### Features

- 📋 Interactive Thanksgiving questionnaire to assess your situation
- 💬 Real-time chat interface with AI-powered coaching
- 🎭 Humorous and sarcastic (but helpful!) responses tailored to your Thanksgiving chaos
- 🚀 Full-stack architecture with separate frontend and backend deployments

---

## 🌐 Live Demo

You can test the complete application here:

**Basic Applications:**
- **Backend**: [https://aie-challenge.vercel.app/](https://aie-challenge)
- **Frontend**: [https://aie-challenge-frontend.vercel.app/](https://aie-challenge-frontend)
- **GitHub**: 
  - [https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)
  - [https://github.com/katgaw/AIM-hot-mess-coach-frontend](https://github.com/katgaw/AIM-hot-mess-coach-frontend)

**Advanced Libraries and UI (Vercel):**
- **Backend Advanced Libraries and UI**: [https://aie-challenge-advanced.vercel.app/](https://aie-challenge-advanced)
- **Frontend Advanced Libraries and UI**: [https://aim-hot-mess-coach-frontend.vercel.app/](https://aie-challenge-frontend-advanced-vercel-backend)
- **GitHub**: 
  - [https://github.com/katgaw/aie-challenge-advanced](https://github.com/katgaw/aie-challenge-advanced)
  - [https://github.com/katgaw/aie-challenge-frontend-advanced](https://github.com/katgaw/aie-challenge-frontend-advanced)

**Advanced Libraries and UI (Render):**
- **Render Backend Advanced Libraries and UI**: [https://aie-challenge-advanced.onrender.com/](https://aie-challenge-advanced.onrender.com/)
- **Frontend Advanced Libraries and UI**: [https://aim-hot-mess-coach-frontend.vercel.app/](https://aie-challenge-frontend-advanced)
- **GitHub**: 
  - [https://github.com/katgaw/aie-challenge-advanced](https://github.com/katgaw/aie-challenge-advanced)
  - [https://github.com/katgaw/aie-challenge-frontend-advanced](https://github.com/katgaw/aie-challenge-frontend-advanced)

---

## Prerequisites

- Python 3.12+
- Node.js 18+ and npm
- OpenAI API key
- Cursor IDE (recommended)
- uv (Python package manager) - optional but recommended

---

## Run Locally

This application consists of two components that need to be run separately:
1. **Backend** (FastAPI) - runs on port 8000
2. **Frontend** (Next.js) - runs on port 3000

### Backend Setup

Navigate to the backend directory:
```bash
cd aie-challenge-hotmess-backend
```

1) Create and activate a local venv
```bash
uv init --python 3.12
```

2) Install dependencies
```bash
uv sync
```

3) Set your OpenAI API key (or create a `.env` file with `OPENAI_API_KEY=...`)
```bash
export OPENAI_API_KEY="sk-..."
```

4) Start the backend server
```bash
uv run uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at http://localhost:8000

**Notes:**
- You can place a `.env` file at the backend root with `OPENAI_API_KEY=...`
- The app entrypoint is `api/index.py` (FastAPI)
- The backend provides a `/api/chat` endpoint for the frontend to consume

---

### Testing the Backend

Once your backend is running, you should test it to verify it works correctly. You can test the deployed backend using curl:

```bash
curl -X POST https://backend-rust-seven-88.vercel.app/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "hi"}'
```

Or test your local backend (make sure it's running on port 8000):

```bash
curl -X POST http://localhost:8000/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "hi"}'
```

You should receive a JSON response with an AI-generated reply. If you get an error, check that:
- Your `OPENAI_API_KEY` is set correctly
- The backend server is running
- Your API key has sufficient credits

---

## Deployment

This section covers deploying your application to production. There are two deployment options:

1. **Basic Deployment** - Deploy both frontend and backend to Vercel (easiest)
2. **Advanced Deployment** - Deploy backend to Render and frontend to Vercel (more flexible)

---

### Basic Deployment: Deploy to Vercel

The simplest way to deploy your application is to use Vercel for both frontend and backend.

#### Deploy Backend to Vercel

1. **Install Vercel CLI** (if you haven't already):
   ```bash
   npm install -g vercel
   ```

2. **Navigate to your backend directory**:
   ```bash
   cd aie-challenge-hotmess-backend
   ```

3. **Deploy to Vercel**:
   ```bash
   vercel --prod
   ```
   Follow the prompts to link your project (or create a new one).

4. **Add Environment Variables**:
   - Go to [https://vercel.com/dashboard](https://vercel.com/dashboard)
   - Select your backend project
   - Go to **Settings** → **Environment Variables**
   - Add `OPENAI_API_KEY` with your OpenAI API key value
   - Select all environments (Production, Preview, Development)
   - Click **Save**

5. **Redeploy** (if needed):
   - Go to **Deployments** tab
   - Click the three dots (⋯) on your latest deployment
   - Click **Redeploy** to apply the environment variable

6. **Copy your backend URL** (e.g., `https://your-backend-name.vercel.app`)

#### Deploy Frontend to Vercel

1. **Navigate to your frontend directory**:
   ```bash
   cd AIM-hot-mess-coach-frontend/frontend-hot-mess-coach
   ```

2. **Deploy to Vercel**:
   ```bash
   vercel --prod
   ```
   Follow the prompts to link your project (or create a new one).

3. **Add Environment Variable**:
   - Go to [https://vercel.com/dashboard](https://vercel.com/dashboard)
   - Select your frontend project
   - Go to **Settings** → **Environment Variables**
   - Add `NEXT_PUBLIC_BACKEND_URL` with your backend URL (e.g., `https://your-backend-name.vercel.app`)
   - Select all environments (Production, Preview, Development)
   - Click **Save**

4. **Redeploy**:
   - Go to **Deployments** tab
   - Click the three dots (⋯) on your latest deployment
   - Click **Redeploy** to apply the environment variable

Your application should now be live! 🎉

---

### Frontend Setup

Navigate to the frontend directory:
```bash
cd AIM-hot-mess-coach-frontend/frontend-hot-mess-coach
```

**Important:** Create a `.env.local` file in this directory and add your public backend URL:
```bash
# Create .env.local file with your deployed backend URL
echo "NEXT_PUBLIC_BACKEND_URL=https://YOUR_BACKEND_URL.vercel.app" > .env.local
```

Replace `YOUR_BACKEND_URL` with your actual deployed backend URL (e.g., `https://backend-rust-seven-88.vercel.app`).

1) Install dependencies
```bash
npm install
```

2) For local development, update `.env.local` to use your local backend:
```bash
# Update .env.local file for local development
echo "NEXT_PUBLIC_BACKEND_URL=http://localhost:8000" > .env.local
```

Or export as environment variable:
```bash
export NEXT_PUBLIC_BACKEND_URL="http://localhost:8000"
```

**Note:** If you want to test against your deployed backend instead, use your public backend URL (as shown in the Important note above).

3) Start the development server
```bash
npm run dev
```

The frontend will be available at http://localhost:3000

**Notes:**
- If `NEXT_PUBLIC_BACKEND_URL` is not set, the frontend will default to the deployed backend URL
- Make sure your backend is running on port 8000 before starting the frontend
- The frontend will auto-reload when you make changes to the code

---

### Advanced Deployment: Backend on Render, Frontend on Vercel

This deployment option gives you more flexibility by using Render for the backend (which supports long-running processes better) and Vercel for the frontend.

#### Deploy Backend on Render

Follow these step-by-step instructions to deploy your backend API to Render:

**Step 1: Create a Render Account**
1. Go to [https://dashboard.render.com/](https://dashboard.render.com/)
2. Sign up for a free account (you can use your GitHub account to sign up)

**Step 2: Create a New Web Service**
1. Once logged in, click the **"+ New"** button in the top right corner
2. Select **"Web Service"** from the dropdown menu

**Step 3: Connect Your GitHub Repository**
1. In the "Connect a repository" section, click **"Connect account"** or **"Configure in GitHub"**
2. Authorize Render to access your GitHub repositories
3. Select the repository that contains your backend code (the one with `api/index.py`)
4. Click **"Connect"**

**Step 4: Configure Your Service Settings**
1. **Name**: Give your service a name (e.g., "aie-challenge-backend")
2. **Region**: Choose the region closest to you (default is fine)
3. **Branch**: Leave as `main` (or your default branch)
4. **Root Directory**: Leave empty (or specify if your backend is in a subdirectory)
5. **Runtime**: Select **"Python 3"** (Render should auto-detect this)
6. **Build Command**: Leave as default (usually `pip install -r requirements.txt`)
7. **Start Command**: **IMPORTANT** - Change this to:
   ```
   uvicorn api.index:app --host 0.0.0.0 --port $PORT
   ```
   (This tells Render how to start your FastAPI application)

**Step 5: Add Environment Variables**
1. Scroll down to the **"Environment"** section
2. Click **"Add Environment Variable"**
3. Add the following:
   - **Key**: `OPENAI_API_KEY`
   - **Value**: Your OpenAI API key (paste it here)
4. Click **"Add"**

**Step 6: Deploy**
1. Scroll to the bottom of the page
2. Click **"Create Web Service"**
3. Render will now build and deploy your application (this takes a few minutes)
4. Wait for the deployment to complete - you'll see a green "Live" status when it's done

**Step 7: Get Your Backend URL**
1. Once deployed, you'll see your service is live
2. Copy the URL at the top of the page (it will look like `https://your-service-name.onrender.com`)
3. **Save this URL** - you'll need it for the frontend configuration

#### Configure Frontend to Connect to Render Backend

After deploying your backend to Render, you need to tell your frontend where to find it:

**Step 1: Go to Your Vercel Project**
1. Go to [https://vercel.com/dashboard](https://vercel.com/dashboard)
2. Find and click on your frontend project

**Step 2: Add Environment Variable**
1. Click on the **"Settings"** tab
2. Click on **"Environment Variables"** in the left sidebar
3. Click **"Add New"**
4. Add the following:
   - **Name**: `NEXT_PUBLIC_BACKEND_URL`
   - **Value**: Your Render backend URL (e.g., `https://your-service-name.onrender.com`)
   - **Environment**: Select all environments (Production, Preview, Development)
5. Click **"Save"**

**Step 3: Redeploy Frontend**
1. After adding the environment variable, go to the **"Deployments"** tab
2. Click the three dots (⋯) on your latest deployment
3. Click **"Redeploy"**
4. This ensures your frontend picks up the new environment variable

Your application should now be fully deployed and connected! 🎉
---

## Quick Start (Both Services)

Open two terminal windows:

**Terminal 1 - Backend:**
```bash
cd aie-challenge-hotmess-backend
export OPENAI_API_KEY="sk-..."
uv run uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd AIM-hot-mess-coach-frontend/frontend-hot-mess-coach
export NEXT_PUBLIC_BACKEND_URL="http://localhost:8000"
npm install
npm run dev
```

Then open http://localhost:3000 in your browser! 🎉

---

## Project Structure

```
aie_challenge_hotmess/
├── aie-challenge-hotmess-backend/    # FastAPI backend
│   ├── api/
│   │   └── index.py                  # Main API endpoints
│   ├── requirements.txt              # Python dependencies
│   └── vercel.json                   # Vercel deployment config
│
└── AIM-hot-mess-coach-frontend/      # Next.js frontend
    └── frontend-hot-mess-coach/
        ├── app/                      # Next.js app directory
        ├── components/               # React components
        │   ├── thanksgiving-chat.tsx
        │   └── thanksgiving-questionnaire.tsx
        └── package.json              # Node.js dependencies
```

---

## Technologies Used

- **Backend**: FastAPI, OpenAI API, Python
- **Frontend**: Next.js, React, TypeScript, Tailwind CSS
- **Deployment**: Vercel

---

## API Endpoints

- `GET /` - Health check endpoint
- `POST /api/chat` - Chat endpoint that accepts a message and returns an AI-generated response

---

## Troubleshooting

**Backend won't start:**
- Ensure `OPENAI_API_KEY` is set correctly
- Check that port 8000 is not already in use
- Verify Python version is 3.12+

**Frontend won't connect to backend:**
- Verify `NEXT_PUBLIC_BACKEND_URL` is set to `http://localhost:8000`
- Ensure the backend is running before starting the frontend
- Check browser console for CORS errors (backend should allow all origins in development)

**OpenAI API errors:**
- Verify your API key is valid and has credits
- Check that the API key has the correct permissions

---

## License

This project is part of the AIE (AI Engineering) curriculum.

