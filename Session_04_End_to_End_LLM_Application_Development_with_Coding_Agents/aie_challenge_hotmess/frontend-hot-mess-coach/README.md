This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

## Deploy Backend on Render

Follow these step-by-step instructions to deploy your backend API to Render:

### Step 1: Create a Render Account
1. Go to [https://dashboard.render.com/](https://dashboard.render.com/)
2. Sign up for a free account (you can use your GitHub account to sign up)

### Step 2: Create a New Web Service
1. Once logged in, click the **"+ New"** button in the top right corner
2. Select **"Web Service"** from the dropdown menu

### Step 3: Connect Your GitHub Repository
1. In the "Connect a repository" section, click **"Connect account"** or **"Configure in GitHub"**
2. Authorize Render to access your GitHub repositories
3. Select the repository that contains your backend code (the one with `api/index.py`)
4. Click **"Connect"**

### Step 4: Configure Your Service Settings
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

### Step 5: Add Environment Variables
1. Scroll down to the **"Environment"** section
2. Click **"Add Environment Variable"**
3. Add the following:
   - **Key**: `OPENAI_API_KEY`
   - **Value**: Your OpenAI API key (paste it here)
4. Click **"Add"**

### Step 6: Deploy
1. Scroll to the bottom of the page
2. Click **"Create Web Service"**
3. Render will now build and deploy your application (this takes a few minutes)
4. Wait for the deployment to complete - you'll see a green "Live" status when it's done

### Step 7: Get Your Backend URL
1. Once deployed, you'll see your service is live
2. Copy the URL at the top of the page (it will look like `https://your-service-name.onrender.com`)
3. **Save this URL** - you'll need it for the frontend configuration

## Configure Frontend to Connect to Backend

After deploying your backend to Render, you need to tell your frontend where to find it:

### Step 1: Go to Your Vercel Project
1. Go to [https://vercel.com/dashboard](https://vercel.com/dashboard)
2. Find and click on your frontend project

### Step 2: Add Environment Variable
1. Click on the **"Settings"** tab
2. Click on **"Environment Variables"** in the left sidebar
3. Click **"Add New"**
4. Add the following:
   - **Name**: `NEXT_PUBLIC_BACKEND_URL`
   - **Value**: Your Render backend URL (e.g., `https://your-service-name.onrender.com`)
   - **Environment**: Select all environments (Production, Preview, Development)
5. Click **"Save"**

### Step 3: Redeploy Frontend
1. After adding the environment variable, go to the **"Deployments"** tab
2. Click the three dots (⋯) on your latest deployment
3. Click **"Redeploy"**
4. This ensures your frontend picks up the new environment variable

Your application should now be fully deployed and connected! 🎉