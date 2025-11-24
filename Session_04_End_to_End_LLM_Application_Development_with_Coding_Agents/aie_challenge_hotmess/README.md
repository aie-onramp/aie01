<p align="center" draggable="false"><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" width="200px" height="auto"/></p>

## <h1 align="center" id="heading">🦃 Hot Mess Coach at Thanksgiving — LLM Application</h1>

An end-to-end LLM application that helps you navigate Thanksgiving challenges with style! This full-stack application features a Next.js frontend with an interactive questionnaire and chat interface, powered by a FastAPI backend that integrates with the OpenAI API to provide personalized, humorous coaching for your Thanksgiving gathering.

### Features

- 📋 Interactive Thanksgiving questionnaire to assess your situation
- 💬 Real-time chat interface with AI-powered coaching
- 🎭 Humorous and sarcastic (but helpful!) responses tailored to your Thanksgiving chaos
- 🚀 Full-stack architecture with separate frontend and backend deployments

---

## 🌐 Live Demo

You can test the complete application here:

**Basic Applications:**
- **Backend**: [https://aie-challenge](https://aie-challenge)
- **Frontend**: [https://aie-challenge-frontend](https://aie-challenge-frontend)
- **GitHub**: 
  - [https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)
  - [https://github.com/katgaw/AIM-hot-mess-coach-frontend](https://github.com/katgaw/AIM-hot-mess-coach-frontend)

**Advanced Libraries and UI (Vercel):**
- **Backend Advanced Libraries and UI**: [https://aie-challenge-advanced](https://aie-challenge-advanced)
- **Frontend Advanced Libraries and UI**: [https://aie-challenge-frontend-advanced-vercel-backend](https://aie-challenge-frontend-advanced-vercel-backend)
- **GitHub**: 
  - [https://github.com/katgaw/aie-challenge-advanced](https://github.com/katgaw/aie-challenge-advanced)
  - [https://github.com/katgaw/aie-challenge-frontend-advanced](https://github.com/katgaw/aie-challenge-frontend-advanced)

**Advanced Libraries and UI (Render):**
- **Render Backend Advanced Libraries and UI**: [https://aie-challenge-advanced.onrender.com/](https://aie-challenge-advanced.onrender.com/)
- **Frontend Advanced Libraries and UI**: [https://aie-challenge-frontend-advanced](https://aie-challenge-frontend-advanced)
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

