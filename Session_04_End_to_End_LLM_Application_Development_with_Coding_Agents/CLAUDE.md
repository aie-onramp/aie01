# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Session 4 focuses on building and deploying end-to-end LLM applications using coding agents. The primary project is the "Hot Mess Coach at Thanksgiving" - a full-stack application with separate FastAPI backend and Next.js frontend components.

**Key Learning Objectives:**
- Deploy Python FastAPI backends to Vercel or Render
- Generate React frontends using v0.dev with backend awareness
- Connect frontend and backend via environment variables
- Test complete full-stack workflows locally and in production

## Development Commands

### Backend (FastAPI)

```bash
# Navigate to backend directory
cd aie_challenge_hotmess/backend-hot-mess-coach

# Initialize Python environment (using uv - recommended)
uv sync

# Set OpenAI API key
export OPENAI_API_KEY="sk-your-api-key-here"

# Run backend locally on port 8000
uv run uvicorn api.index:app --reload --host 0.0.0.0 --port 8000

# Test backend health
curl http://localhost:8000

# Test chat endpoint
curl -X POST http://localhost:8000/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello, Hot Mess Coach!"}'

# Deploy to Vercel
vercel --prod
```

**Alternative (using venv + pip):**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate  # On Windows
pip install -r requirements.txt
uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

### Frontend (Next.js)

```bash
# Navigate to frontend directory
cd aie_challenge_hotmess/frontend-hot-mess-coach

# Install dependencies
npm install

# Configure backend URL for local development
export NEXT_PUBLIC_BACKEND_URL="http://localhost:8000"
# OR create .env.local:
echo "NEXT_PUBLIC_BACKEND_URL=http://localhost:8000" > .env.local

# Run frontend locally on port 3000
npm run dev

# Build for production
npm run build

# Deploy to Vercel
vercel --prod
```

### Quick Start (Both Services)

Run in two terminal windows simultaneously:

**Terminal 1 - Backend:**
```bash
cd aie_challenge_hotmess/backend-hot-mess-coach
export OPENAI_API_KEY="sk-..."
uv run uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd aie_challenge_hotmess/frontend-hot-mess-coach
export NEXT_PUBLIC_BACKEND_URL="http://localhost:8000"
npm install
npm run dev
```

Then visit http://localhost:3000

## High-Level Architecture

### Full-Stack Application Structure

```
Session_04/
├── aie_challenge_hotmess/
│   ├── backend-hot-mess-coach/         # FastAPI backend
│   │   ├── api/
│   │   │   └── index.py                # Main API with /api/chat endpoint
│   │   ├── pyproject.toml              # Python dependencies (uv)
│   │   ├── requirements.txt            # Python dependencies (pip)
│   │   └── vercel.json                 # Routes all requests to api/index.py
│   │
│   └── frontend-hot-mess-coach/        # Next.js frontend (v0-generated)
│       ├── app/
│       │   ├── page.tsx                # Main page with state management
│       │   └── layout.tsx              # Root layout
│       ├── components/
│       │   ├── thanksgiving-questionnaire.tsx
│       │   └── thanksgiving-chat.tsx   # Chat interface
│       └── package.json                # Node dependencies
│
├── Assignment.md                       # Step-by-step assignment instructions
├── BreakoutRoom.md                     # Hands-on workshop guide
└── README.md                           # Session overview
```

### Backend Architecture

**Technology Stack:**
- FastAPI for REST API endpoints
- OpenAI Python SDK for GPT-4o-mini integration
- CORS middleware configured to allow all origins
- Pydantic models for request validation

**Key API Endpoints:**
- `GET /` - Health check endpoint
- `POST /api/chat` - Accepts `{"message": "text"}`, returns `{"reply": "AI response"}`
- `GET /api/chat` - Returns error with usage instructions

**Environment Requirements:**
- `OPENAI_API_KEY` - Required for OpenAI API calls

### Frontend Architecture

**Technology Stack:**
- Next.js 16 with App Router
- React 19 with TypeScript
- shadcn/ui components (Radix UI primitives)
- Tailwind CSS for styling
- Lucide React for icons

**Application Flow:**
1. User fills out Thanksgiving questionnaire (family size, chaos level, etc.)
2. Questionnaire data stored in React state
3. Chat interface displays with user info context
4. Messages sent to backend via POST to `NEXT_PUBLIC_BACKEND_URL/api/chat`
5. AI responses rendered in chat UI

**Environment Requirements:**
- `NEXT_PUBLIC_BACKEND_URL` - Backend API base URL (http://localhost:8000 for local, Vercel URL for production)

### Deployment Architecture

**Vercel Deployment (Primary):**
- Backend and frontend deployed as separate Vercel projects
- Environment variables configured in Vercel dashboard
- Automatic deployments on git push

**Render Deployment (Alternative for Backend):**
- Backend can be deployed to Render for better long-running process support
- Start command: `uvicorn api.index:app --host 0.0.0.0 --port $PORT`
- Frontend remains on Vercel, configured with Render backend URL

## Important Context

### AI-Assisted Development Workflow

This session emphasizes using AI coding agents (Cursor) and AI frontend generators (v0.dev):

1. **Backend from AIE-Challenge:** Students pull pre-built FastAPI backend from upstream repository
2. **Frontend via v0.dev:** Students provide backend API details to v0.dev and generate React UI
3. **Cursor for Customization:** Students use Cursor AI to modify, connect, and debug

### Environment Variable Management

**Critical for deployment success:**

Backend needs:
- `OPENAI_API_KEY` set in Vercel/Render dashboard

Frontend needs:
- `NEXT_PUBLIC_BACKEND_URL` set to deployed backend URL
- Local development uses `http://localhost:8000`
- Production uses full Vercel/Render URL

**Common pitfall:** Forgetting to redeploy after adding environment variables in Vercel dashboard

### Testing Strategy

**Test backend before frontend:**
1. Deploy backend first
2. Test with curl to verify API works
3. Then deploy frontend with correct `NEXT_PUBLIC_BACKEND_URL`

**Test locally before deploying:**
1. Run backend on :8000
2. Run frontend on :3000 with local backend URL
3. Verify end-to-end flow works
4. Then deploy to production

### Repository Setup Pattern

Students create their own repository and add AIE-challenge as upstream:
```bash
git clone git@github.com:USERNAME/aie-challenge-hotmess.git
cd aie-challenge-hotmess
git remote add upstream https://github.com/AI-Maker-Space/aie-challenge-hotmess.git
git fetch upstream
git pull upstream main --allow-unrelated-histories
```

## v0.dev Integration

### Generating Frontend with v0

**Recommended prompt structure:**
```
Create a frontend called "Hot Mess Coach UI" for a Thanksgiving coaching application.

This frontend must call my backend:
POST https://YOUR_BACKEND_URL.vercel.app/api/chat

Request Body: {"message": "text"}
Response: {"reply": "AI-generated response"}

Requirements:
- React + Next.js + TypeScript + Tailwind CSS
- shadcn/ui components
- Interactive questionnaire (family size, chaos level, etc.)
- Chat interface with loading states
- Thanksgiving theme with humorous UI
- Mobile responsive
```

**Best practice:** Upload backend `api/index.py` to v0.dev for API context

### Integrating v0 Code

After downloading from v0.dev:
1. Extract the zip file
2. Move to frontend directory structure
3. Run `npm install` to install dependencies
4. Configure environment variables
5. Test locally before deploying

## Troubleshooting

### Backend Issues

**"OPENAI_API_KEY not configured" error:**
- Verify environment variable is set in deployment platform
- Redeploy after adding environment variable
- Check API key has credits and correct permissions

**Port already in use:**
- Kill process on port 8000: `lsof -ti:8000 | xargs kill -9`
- Or use different port: `--port 8001`

**CORS errors:**
- Backend already configured with `allow_origins=["*"]` for development
- If still seeing errors, check backend logs for actual issue

### Frontend Issues

**Cannot connect to backend:**
- Verify `NEXT_PUBLIC_BACKEND_URL` is set correctly
- Check backend is running (local) or deployed (production)
- Inspect browser console for actual error messages
- Verify URL has no trailing slash

**Environment variable not updating:**
- Must restart `npm run dev` after changing `.env.local`
- Must redeploy in Vercel after changing environment variables

**Build errors:**
- Check all imports are correct
- Run `npm install` to ensure dependencies are installed
- Check for TypeScript errors with `npm run lint`

### Deployment Issues

**Vercel deployment fails:**
- Check build logs in Vercel dashboard
- Verify `vercel.json` is correctly configured for backend
- Ensure `requirements.txt` or `pyproject.toml` includes all dependencies
- For frontend, ensure `package.json` has correct Next.js version

**Backend works locally but not deployed:**
- Verify `OPENAI_API_KEY` is set in Vercel environment variables
- Check Vercel function logs for error details
- Ensure API key has credits

**Frontend deployed but can't reach backend:**
- Verify `NEXT_PUBLIC_BACKEND_URL` is set in Vercel environment variables
- Check that backend URL is correct (no typos)
- Test backend URL directly with curl
- Redeploy frontend after adding environment variable
