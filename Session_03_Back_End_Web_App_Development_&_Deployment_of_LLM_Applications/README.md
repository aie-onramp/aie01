<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Session 3: Back End Web App Development & Deployment of LLM Applications</h1>

| 🤓 Pre-class | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
|[Prepare Backend](https://github.com/AI-Maker-Space/AIEO1/tree/main/03_Prepare_Session_03_Backend) | [Recording!](https://us02web.zoom.us/rec/share/ZC-WtdQNkORmgkLGNgnii4HF3m--tkD6eS1S26Jgby-DhWUqqzq2kN-m9cZHnsOJ.62QKCGJZNrUeguwD) (6+hv2YpS) | [Slides](https://www.canva.com/design/DAG492HUYsU/d98h86nIBAbpLsJ2TBFriQ/edit?utm_content=DAG492HUYsU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [HW #3](https://forms.gle/44PKtYxPhL3xUiJg7) | [Mon, Nov 24](https://forms.gle/moKSGEmZacqA63c36) |

---

## Prerequisites

- Python 3.10+
- Cursor IDE
- GitHub account
- Vercel account
- uv (Python package manager)
- OPENAI_API_KEY (set as an environment variable in Vercel)
- Optional: Vercel CLI (only if deploying from terminal):
  ```bash
  npm install -g vercel
  ```


In today's code, we also use several new tools and frameworks:
- [OpenAI API](https://platform.openai.com/docs/guides/text)
- [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [HTML](https://www.w3schools.com/html/)
- [Streamlit](https://docs.streamlit.io/get-started/fundamentals/main-concepts) 

Note: You are **not expected or required** to know these yet; this list is simply here for reference and exploration.


---

# Build 🏗️

In this session, you'll build a Python FastAPI backend called Hot Mess Coach, add an LLM chat endpoint, optionally add document analysis (PDF/CSV), and deploy to Vercel. Advanced: generate a frontend in v0 and connect it to your backend.

- 🤝 [Breakout Room](./BreakoutRoom.md)
    - Add GitFlow and Cursor rules
    - Create GitHub repo
    - Add a FastAPI backend
    - Run locally
    - Deploy the backend to Vercel

- 🤝 [Assignment](./Assignment.md)
    - Set up environment and create FastAPI
    - Add extra features
    - Test locally and deploy to Vercel
    - Advanced: generate a frontend in v0, connect to backend, deploy frontend

# Ship 🚢

The deployed Hot Mess Coach backend on Vercel (and optional frontend connected to it)!

Our deployed Vercel applications are here: 
1. https://aim-hot-mess-coach.vercel.app/
   with GitHub repo available here: https://github.com/katgaw/AIM-hot-mess-coach
2. https://aim-hot-mess-coach-upload.vercel.app/
    with GitHub repo available here: https://github.com/katgaw/AIM-hot-mess-coach-upload

<details>
<summary>🚧 Advanced Modules (OPTIONAL) — <i>open for details</i></summary>

**Advanced Backend:**
- Add PDF/CSV uploads and structured analysis
- Implement chunking utilities for long documents
- Iterate locally, then re-deploy

**Advanced Frontend (v0):**
- Generate a frontend with v0 that calls your backend (`POST /chat`)
- Connect via fetch and deploy the frontend to Vercel

</details>

### Deliverables

- A short Loom of either:
  - Your deployed backend (and optional frontend) showcasing the features you built
  - A walkthrough of your GitFlow + multi-agent workflow
  - Your advanced module (doc analysis/chunking or v0 frontend)

# Share 🚀

Make a social media post about your final application!

### Deliverables

- Make a post on any social media platform about what you built!

Here's a template to get you started:

```
🚀 Exciting News! 🚀

I am thrilled to announce that I have just built and deployed a modern web application using AI-powered development tools! 🎉🤖

🔍 Three Key Takeaways:

1️⃣ AI tools like v0.dev can generate complete frontend applications from natural language prompts

2️⃣ GitFlow and feature branching enable parallel development workflows

3️⃣ Modern CI/CD with Vercel makes deployment seamless and automatic

Let's continue pushing the boundaries of what's possible in the world of AI-assisted development. Here's to many more innovations! 🚀

Check out my app: [Your Vercel URL]

Shout out to @AIMakerspace !

#WebDevelopment #AI #Frontend #React #NextJS #Vercel #Innovation #TechMilestone

Feel free to reach out if you're curious or would like to collaborate on similar projects! 🤝🔥
```
