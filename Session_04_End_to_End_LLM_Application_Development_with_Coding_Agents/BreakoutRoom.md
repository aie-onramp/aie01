# 🚀 Breakout Room #1: Build & Deploy Your Full-Stack App – *Hot Mess Coach*

Welcome! In this breakout room you'll build a complete full-stack application—deploy a **Python FastAPI backend** (from Session 3 in AIEO1), create a **React.js frontend** using v0, and connect them together on **Vercel**.

---

## 📚 Table of Contents

- [What Is This Demo?](#what-is-this-demo)
- [Prerequisites](#prerequisites)
- [Step 1: Create Empty Repository](#step-1-create-empty-repository)
- [Step 2: Set Up Backend from AIE-Challenge](#step-2-set-up-backend-from-aie-challenge)
- [Step 3: Test Backend Locally & Deploy to Vercel](#step-3-test-backend-locally--deploy-to-vercel)
- [Step 4: Create v0 Frontend](#step-4-create-v0-frontend)
- [Step 5: Test Frontend Locally & Deploy to Vercel](#step-5-test-frontend-locally--deploy-to-vercel)
- [Step 6: Connect Frontend to Backend](#step-6-connect-frontend-to-backend)
- [Step 7: Test Your Full-Stack App](#step-7-test-your-full-stack-app)

---

## Prerequisites

- Python 3.10+
- Node.js 18+ and npm
- Cursor IDE
- GitHub account
- Vercel account
- v0 account (for frontend generation)
- uv (Python package manager)
- OPENAI_API_KEY (set as an environment variable in Vercel)
- Optional: Vercel CLI (only if deploying from terminal):
  ```bash
  npm install -g vercel
  ```

---

## 🤝 Breakout Room #1

A full hands-on session where you'll deploy both backend and frontend, then connect them together on Vercel.

---

# What Is This Demo?

Students will:

- Create a new repository and set up the backend from AIE-challenge
- Deploy a FastAPI backend to Vercel
- Create a React.js frontend using v0
- Deploy the frontend to Vercel
- Connect frontend to backend
- Test the complete full-stack application

---

# 📝 Step 1: Create Empty Repository

1. Go to GitHub and create a new empty repository (e.g., `hot-mess-coach`)
2. Clone it locally:

```bash
git clone {your_repo_ssh_or_https_url}
cd hot-mess-coach
```

---

# 🔄 Step 2: Set Up Backend from AIE-Challenge

1. Add the AIE-challenge repository as a remote:

```bash
git remote add upstream {AIE-challenge_repo_ssh_or_https_url}
```

2. Fetch the backend code from the AIE-challenge repository:

```bash
git fetch upstream
```

3. Copy the backend files from the AIE-challenge repository. The backend structure should include:
   - `api/index.py` (FastAPI application from Session 3)
   - `requirements.txt` or `pyproject.toml`
   - `vercel.json` (for Vercel deployment)

You can either:
   - Copy files manually from the upstream repository
   - Or checkout specific files: `git checkout upstream/main -- api/`

4. Set up your backend structure:

```bash
# Create api directory if it doesn't exist
mkdir -p api

# Copy backend files (adjust paths as needed based on AIE-challenge structure)
# Example: if backend is in aie-challenge/backend/
# cp -r ../aie-challenge/backend/* api/

# Install dependencies
cd api
uv sync  # or: pip install -r requirements.txt
cd ..
```

5. Push to your own repository:

```bash
git add .
git commit -m "Initial commit: Add backend from AIE-challenge"
git push origin main
```

---

# 🐍 Step 3: Test Backend Locally & Deploy to Vercel

## Test Locally

Run the backend locally:

```bash
# From your project root
uv run uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

Or if using pip:

```bash
uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

Visit:

- http://localhost:8000  
- http://localhost:8000/docs (FastAPI Swagger UI)

Test the endpoints to make sure everything works!

## Deploy to Vercel

1. Make sure all changes are committed and pushed:

```bash
git add .
git commit -m "Ready for Vercel deployment"
git push origin main
```

2. Deploy to Vercel:

```bash
vercel --prod
```

Or deploy via Vercel dashboard:
- Go to Vercel dashboard
- Import your GitHub repository
- Configure build settings (Vercel should auto-detect FastAPI)
- Add environment variable: `OPENAI_API_KEY`

3. **Important**: Make sure to add your `OPENAI_API_KEY` as an environment variable in Vercel project settings!

4. Note your backend URL (e.g., `https://your-backend.vercel.app`)

---

# 🎨 Step 4: Create v0 Frontend

1. Go to [v0.dev](https://v0.dev) and sign in

2. Use this prompt (or customize it):

```
I want you to create react.js frontend for 'HotMessCoach at Thanksgiving' that will help user to deal with the thanksgiving stress by giving a chatting opportunity with this coach. The chatting backend is attached in index.py. Make the app fun so everyone laughs, add there also functioning frontend select bars for user to select how many family members are coming (make even these questions fun) and then the chatting window following the filled-in Q&A. Make sure there is an image of a large fun and very upset turkey. Use this button style: 

import { ArrowUpIcon } from "lucide-react"
import { Button } from "@/components/ui/button"

export function ButtonDemo() {
  return (
    <div className="flex flex-wrap items-center gap-2 md:flex-row">
      <Button variant="outline">Button</Button>
      <Button variant="outline" size="icon" aria-label="Submit">
        <ArrowUpIcon />
      </Button>
    </div>
  )
}

Use color scheme from coolors.co
```

3. Attach your `api/index.py` file to provide context about the backend API

4. Generate the frontend code in v0

5. Copy the generated code to your local repository

6. Create a frontend directory structure (e.g., `frontend/` or integrate into root):

```bash
# Option 1: Separate frontend folder
mkdir frontend
# Copy v0 generated files into frontend/

# Option 2: Integrate into root (Next.js structure)
# Copy v0 files to root, maintaining Next.js structure
```

---

# ⚛️ Step 5: Test Frontend Locally & Deploy to Vercel

## Test Locally

1. Navigate to your frontend directory:

```bash
cd frontend  # or root if integrated
```

2. Install dependencies:

```bash
npm install
```

3. Run the development server:

```bash
npm run dev
```

4. Visit http://localhost:3000 (or the port shown)

5. Test the frontend UI locally

## Deploy Frontend to Vercel

1. Commit your frontend code:

```bash
git add .
git commit -m "Add v0 frontend"
git push origin main
```

2. Deploy to Vercel:

```bash
# If frontend is in a subdirectory, specify it:
vercel --prod --cwd frontend

# Or deploy via Vercel dashboard:
# - Create a new project in Vercel
# - Point to your repo
# - Set root directory to 'frontend' if applicable
```

3. Note your frontend URL (e.g., `https://your-frontend.vercel.app`)

---

# 🔗 Step 6: Connect Frontend to Backend

1. Update your frontend API configuration to point to your deployed backend:

   - Find where API calls are made in your frontend code
   - Update the base URL to your Vercel backend URL
   - Example: Change `http://localhost:8000` to `https://your-backend.vercel.app`

2. If using environment variables (recommended):

   - Create a `.env.local` file in your frontend directory:
     ```
     NEXT_PUBLIC_API_URL=https://your-backend.vercel.app
     ```

   - Update your frontend code to use `process.env.NEXT_PUBLIC_API_URL`

3. Update Vercel environment variables for your frontend project:
   - Go to Vercel dashboard → Your frontend project → Settings → Environment Variables
   - Add `NEXT_PUBLIC_API_URL` with your backend URL

4. Commit and redeploy:

```bash
git add .
git commit -m "Connect frontend to backend"
git push origin main
vercel --prod --cwd frontend  # or redeploy via dashboard
```

---

# ✅ Step 7: Test Your Full-Stack App

1. Visit your deployed frontend URL

2. Test the complete flow:
   - Fill in the questionnaire (number of family members, etc.)
   - Start chatting with the Hot Mess Coach
   - Verify messages are sent to and received from the backend
   - Check that the turkey image displays correctly
   - Test all interactive elements

3. Check browser console for any errors

4. Verify backend logs in Vercel dashboard if needed

5. Celebrate! 🎉 Your full-stack app is live!

---

# 🏗️ Next Steps & Customization

Now that your app is deployed and connected, you can:

- Customize the UI styling and colors
- Add more features to the chat
- Enhance the questionnaire
- Add error handling and loading states
- Implement authentication if needed
- Add more backend endpoints
- Follow GitFlow best practices for future changes

Enjoy building your full-stack AI app! 🎉
