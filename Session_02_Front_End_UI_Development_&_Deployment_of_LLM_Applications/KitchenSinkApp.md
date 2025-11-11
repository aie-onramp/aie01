# One Shot Prompt to create gdelt-ui-demo

-https://gdelt-ui-demo.vercel.app/

# Input to ChatGPT

Create a prompt for the v0 application to generate a UI for the following application using the prompt template.

APPLICATION:  https://github.com/aie8-cert-challenge/gdelt-knowledge-base
PROMPT TEMPLATE:
```
Create me an app: [Your App Name]

[Description of your app concept]

Use the design style similar to: [Canva template reference]
For components, use shadcn/ui with: [component names]
Color scheme: [your colors from Coolors]
```

---

## One shot example

Welcome! This guide will walk you through two demos that showcase modern development workflows using v0, Cursor, and best practices. We'll complete these together during the breakout session, and you can continue on your own afterward if we don't finish.

### What You'll Be Working On?

We will build and deploy modern web applications using AI-powered development tools. You'll learn to leverage v0 (an AI tool for generating frontend code), Cursor IDE (an AI-enhanced code editor), and industry-standard deployment practices with GitHub and Vercel.

**You will master:**
- **AI-Powered Development:** Use v0 to generate complete frontend applications from natural language prompts
- **Professional Workflow:** Implement GitFlow branching strategies and coding standards using Cursor's AI capabilities
- **Multi-Agent Development:** Simulate parallel development workflows by working on multiple features simultaneously
- **Full Deployment Pipeline:** Push code to GitHub and deploy live applications to Vercel with automatic CI/CD

By the end, you'll have created, customized, and deployed your own live web application while learning modern development practices that mirror real-world team workflows. The hands-on exercises progress from basic UI customization to advanced multi-branch development, giving you practical experience with the tools and techniques used in professional software development.

---

### 📚 Table of Contents

- [What You'll Be working On?](#what-you'll-be-working-on)
- [Prerequisites](#prerequisites)
- [Overview](#overview)
- [Step 1: Brainstorm Your Idea 💡](#step-1-brainstorm-your-idea-)
- [Step 2: Get Your Design Resources 🎨](#step-2-get-your-design-resources-)
- [Step 3: Create Your v0 Prompt 🎬](#step-3-create-your-v0-prompt-)
- [Step 4: Set Up Cursor Rules 📝](#step-4-set-up-cursor-rules-)
- [Step 5: Download Your App from v0 📥](#step-5-download-your-app-from-v0-)
- [Step 6: Generate README with Cursor 🤖](#step-6-generate-readme-with-cursor-)
- [Step 7: Set Up and Run Locally 🏃](#step-7-set-up-and-run-locally-)
- [Step 8: Push to GitHub 🐙](#step-8-push-to-github-)
- [Step 9: Deploy to Vercel 🌐](#step-9-deploy-to-vercel-)
- [🏗️ Activity #1](#️-activity-1)

---

### Prerequisites

Before we begin, make sure you have:
- [Cursor](https://cursor.sh/) installed
- A [GitHub](http://github.com/) account
- A [Vercel](https://vercel.com/) account (free tier works great!)
- Install the Vercel CLI in Cursor: `npm install -g vercel`
- Node.js installed on your computer (use Mac: `brew install node`, Windows: `sudo apt install nodejs npm`)

---

### 🤝 Breakout Room: Creating and Deploying Your Frontend Application

#### Overview

In this session, we'll:
1. **Showcase v0** - create a vibecode frontend using personal practices
2. **Showcase Cursor rules** by adding GitFlow rules and personal cursor rules (coding styles) to improve collaboration
3. **Download and showcase locally** - run the app on your machine
4. **Push to GitHub and deploy to Vercel** - get your app live on the web

---

#### Step 1: Brainstorm Your Idea 💡

First, you need an idea for your app! You have two options:

**Option A: Use v0 for brainstorming**
- Go to [v0.dev](https://v0.dev)
- Use the chat to explore ideas and get suggestions

**Option B: Use ChatGPT (Recommended)**
- Ask ChatGPT to help you brainstorm app ideas
- Get feedback on your concept
- Refine your idea until you're happy with it

---

#### Step 2: Get Your Design Resources 🎨

Now it's time to gather design inspiration and components. You have two paths:

##### Path A: Use v0's Premade Templates
- Browse v0's template library
- Pick a template that matches your vision

##### Path B: Create Your Own Design (More Original!)

**a) Pick a Template Style:**
- Visit [Canva Templates](https://www.canva.com/templates/)
- Find a design style you like
- Note the colors, layout, and overall aesthetic

**b) Choose Component Styles:**
- Go to [shadcn/ui Components](https://ui.shadcn.com/docs/components/)
- Browse the component library
- Pick components that match your app's needs (buttons, cards, forms, etc.)

**c) Select a Color Scheme:**
- Visit [Coolors](https://coolors.co/)
- Generate or browse color palettes
- Pick colors that match your app's mood and purpose

---

#### Step 3: Create Your v0 Prompt 🎬

Now combine everything into a detailed prompt for v0:

1. Describe your app idea
2. Reference the template style you chose
3. Mention the shadcn/ui components you want to use
4. Include your color scheme
5. Add any specific features or requirements

**Example prompt structure:**
```
Create me an app: [Your App Name]

[Description of your app concept]

Use the design style similar to: [Canva template reference]
For components, use shadcn/ui with: [component names]
Color scheme: [your colors from Coolors]
```

---

#### Step 4: Set Up Cursor Rules 📝

##### 4.1 Add GitFlow Rules

Set up GitFlow rules to maintain clean version control:

1. Open your project in Cursor
2. Navigate to `gitflow_rules.md` (or create it if it doesn't exist)
3. Add your project-specific GitFlow rules
4. This helps maintain clean version control throughout development

**Example GitFlow rules:**
- Branch naming conventions
- Commit message formats
- Merge strategies
- Release workflow

##### 4.2 Add Personal Cursor Rules (Coding Styles)

Set up coding style rules to improve collaboration:

1. Create or update `cursor_rules.md` in your project
2. Add coding standards such as:
   - Code structure & organization
   - Naming conventions (camelCase, PascalCase, UPPER_SNAKE_CASE)
   - Import paths
   - File size limits
   - Component organization

**Why this matters:** These rules help Cursor understand your coding preferences and maintain consistency across your project, making collaboration smoother.

---
#### Step 5: Download Your App from v0 📥

1. In v0, after generating your app, click **"Download"**
2. Copy the download command or use the provided link
3. In Cursor's terminal, run the download command
4. This will create your app folder with all the code

---

#### Step 6: Generate README with Cursor 🤖

Let Cursor help you create documentation:

1. In Cursor, ask: *"Create a README.md file explaining how to launch this app"*
2. Cursor will analyze your project structure
3. It will generate a README with setup and launch instructions
4. Review and customize as needed

---

#### Step 7: Set Up and Run Locally 🏃

##### 7.1 Navigate to App Directory
```bash
cd app
```

##### 7.2 Install Dependencies
```bash
npm install
```

This installs all the packages your app needs to run.

##### 7.3 Run Your App Locally
```bash
npm run dev
```

Your app should now be running! Look for a local URL (usually `http://localhost:3000`) in the terminal.

**Showcase your app locally!** Open the URL in your browser and see your creation come to life.

---

#### Step 8: Push to GitHub 🐙

1. Create a new repository on GitHub
2. In Cursor terminal, initialize git (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
3. Add your GitHub repository as remote:
   ```bash
   git remote add origin https://github.com/yourusername/yourrepo.git
   ```
4. Push your code:
   ```bash
   git push -u origin main
   ```

---

#### Step 9: Deploy to Vercel 🌐

1. Go to [Vercel](https://vercel.com)
2. Sign in with your GitHub account
3. Click **"New Project"**
4. Import your GitHub repository
5. Vercel will automatically detect your framework
6. Click **"Deploy"**
7. Wait a few minutes, and your app will be live! 🎉

**Your app is now deployed and accessible to the world!**

---

#### 💅 Example: "Hot Mess Tracker" App

> 🌐 **Live Demo:** You can view the deployed app here: [https://v0-hot-mess-tracker-app.vercel.app/](https://v0-hot-mess-tracker-app.vercel.app/)

Here's the complete prompt we'll use in class for our example app:

##### App Prompt for v0:

```
Create me an app: "Hot Mess Tracker"

A "self-report" app for chaos level of your day.

Concept:
- Sliders: "Late to class," "Lost charger," "Sent risky text," "Procrastination"
- Animated emoji face reacts as your "hot mess score" increases
- Saves your results and gives sarcastic motivational message like: "At least you're consistently chaotic. We love that for you"

Design Requirements:
- Use the website style similar to: https://www.canva.com/templates/EAFSoi3Ltnc/
- Similar style background
- For buttons, use this style:

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

Color Scheme (for Tailwind CSS):
- murrey: #89023e (hsla(333, 97%, 27%, 1))
- old-rose: #cc7178 (hsla(355, 47%, 62%, 1))
- misty-rose: #ffd9da (hsla(358, 100%, 93%, 1))
- misty-rose-2: #f3e1dd (hsla(11, 48%, 91%, 1))
- tea-green: #c7d9b7 (hsla(92, 31%, 78%, 1))
```

##### Tailwind Color Configuration

Add these colors to your `tailwind.config.js`:

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        'murrey': '#89023e',
        'old-rose': '#cc7178',
        'misty-rose': '#ffd9da',
        'misty-rose-2': '#f3e1dd',
        'tea-green': '#c7d9b7',
      }
    }
  }
}
```

---

#### 🛠️ Debugging: npm install errors (local or Vercel)

If you encounter an `npm install` error:

1. Install with legacy peer deps:
   ```bash
   npm install --legacy-peer-deps
   ```
2. Uninstall `vaul` (problematic peer dependency in some templates):
   ```bash
   npm uninstall vaul
   ```
3. Commit the resulting dependency updates:
   ```bash
   git add package.json package-lock.json
   git commit -m "Fix install with --legacy-peer-deps and remove vaul"
   git push
   ```
4. Redeploy on Vercel. The build should now pass.

For local: if port 3000 is in use, free it first:
```bash
kill -9 $(lsof -ti tcp:3000)
```
---
#### 🏗️ Activity #1:

Now it's your turn to experiment and get creative! Use this time to practice what you've learned and explore the tools.

**Experiment with Design Customization:**
- Test out different background styles and color schemes
- Try different button styles and components from shadcn/ui
- Make design changes using v0 to see how it generates updated code
- Practice iterating on your app's visual design

---

# ChatGPT response - Used as input to v0 app

Create me an app: **GDELT Knowledge Graph RAG Assistant**

An interactive frontend for exploring and explaining the `gdelt-knowledge-base` project.

The app should:

* Present a **hero overview** of the GDELT Knowledge Graph RAG Assistant: what it does, architecture layers, and how it uses LangGraph + multi-retriever RAG + RAGAS evaluation + manifests for provenance.
* Provide a **Query Console** page:

  * Left: input panel for “Ask about GDELT docs / pipeline / datasets”.
  * Right: chat-style response area showing:

    * Answer text
    * Retrieved context snippets
    * Active retriever strategy (naive, BM25, ensemble, cohere_rerank)
    * Provenance badges (dataset, SHA, manifest links).
* Provide an **Evaluation Dashboard** page:

  * Cards for key metrics (Faithfulness, Answer Relevancy, Context Precision, Context Recall).
  * Comparison table & chart for retrievers using sample data from `RUN_MANIFEST` and RAGAS outputs.
* Provide a **Datasets & Manifests** page:

  * Cards for each Hugging Face dataset with description and “View details” buttons.
  * Timeline/stack view for ingestion manifest → run manifest → evaluation outputs to highlight lineage.
* Provide an **Architecture Explorer** page:

  * Visual layout of the 5-layer architecture
  * Cards for each layer (Config, Data, Retrieval, Orchestration, Execution) with key modules.
* Use a **persistent sidebar + top nav** with clear sections:

  * Overview, Query, Evaluation, Datasets, Architecture, Docs (linking to repo docs).

Use the design style similar to:
A modern data-storytelling & analytics dashboard template such as a **Canva “Data Analytics Dashboard / Tech Case Study” landing page** (clean, minimal, card-based, with subtle gradients and plenty of white space).

For components, use shadcn/ui with:

* `app-shell` style layout using `Sheet` or `Sidebar`, `Navbar`, `Breadcrumb`
* `Card`, `Badge`, `Separator`, `Tabs`, `Accordion` for architecture & docs
* `Table` for RAGAS metrics & retriever comparisons
* `Input`, `Textarea`, `Select`, `Button` for the query console
* `Alert` / `Callout` for provenance warnings or notes
* `Tooltip`, `HoverCard` to explain metrics and retriever strategies
* Optional: `Skeleton` states for loading, `ScrollArea` for context snippets

Color scheme (Coolors-style palette, Tailwind-friendly):

* Background: `#020817` (deep navy)
* Surface: `#0f172a` and `#111827` (slate panels)
* Primary accent: `#38bdf8` (sky blue) for CTAs & active states
* Secondary accent: `#14b8a6` (teal) for metrics & links
* Highlight accent: `#f97316` (orange) for key scores and warnings
* Text & borders: `#e5e7eb` and `#9ca3af` for readable contrast

Make the layout production-ready:

* Responsive (desktop-first dashboard, clean mobile collapse).
* Clear visual hierarchy emphasizing **query → evidence → metrics → provenance**.
* All sections structured so a real backend (LangGraph server + evaluation APIs) can be wired in with minimal changes.


-----------------------

# v0 Project - used to create new github project

```bash
npx create-next-app gdelt-ui-demo
cd gdelt-ui-demo
npx shadcn@latest init
```

```bash
# Example import command for v0-generated components
# (token expires after ~24h; replace with your own when re-running)
npx shadcn@latest add "https://v0.app/chat/b/b_Gxxaos4yxDs?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..GKctd6FxeJGfAgud.VYQEO77jvtq3aJrj3pydSSzyGz2aSmI09tkjkuyENK6bze2VrdFaeelq_cE.ne3wmziTSXs6S4ztD5dwWQ"
```

