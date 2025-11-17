# **🚢 Session 3 Overview: Backend Development**

In this session, we’ll learn how to build a FastAPI backend and deploy it to Vercel.  

We’ll also demonstrate where Vercel’s deployment solutions start to break down as our applications grow in complexity, which will be important to keep in mind as your backends continue to grow in capabilities!

## 📛 Required **Tooling & Account Setup**

The required tooling and account setup is the same as Session 2!

1. 🧑‍💻 Ensure [Cursor](https://cursor.com/) is installed and [GitHub](https://github.com/) is set up.
2. 🚀 Create a [Vercel](https://vercel.com/) account (free tier).
3. 🖼️ Install Node.js on your computer 
    1. Mac: `brew install node`
    2. Windows: `sudo apt install nodejs npm`
4. 💻 Install the Vercel CLI in Cursor: `npm install -g vercel` **only required for advanced build*

## 🧑‍💻 Recommended Pre-Work!

1. 📚 Read:
    1. Review the [FastAPI homepage](https://fastapi.tiangolo.com/) and think about lessons not yet learned.
    2. [FastAPI on Vercel](https://vercel.com/docs/frameworks/backend/fastapi) (updated October 15, 2025)

## **🤔 Concepts**

We will build on the core concepts from Session 1 and Session 2, primarily adding two big ideas:

1. Adopting a [Python Web Framework](https://wiki.python.org/moin/WebFrameworks) for building out the backend of our applications
2. A simple development pattern:
    1. Building out features outside of your application (e.g., within a notebook)
    2. Integrating features we’ve constructed into our application’s backend
    3. Deploying our backend to a publicly accessible endpoint

## ⌨️ **Code**

The **code** for this session should be understood in the sequence it’s presented. We will build out FastAPI backends that are:

- Deployed locally, with direct HTML output
- Deployed locally, connected to an OpenAI API endpoint (e.g., to an LLM)
- Deployed locally, connected to LLM with direct HTML output
- Deployed remotely to Vercel, connected to an LLM with direct HTML output

We will also demonstrate how to continue to build out more advanced backends that are:

- Deployed locally, connected to LLM with simple [Streamlit](https://streamlit.io/) frontend
- Deployed locally, with `.csv` and `.pdf` upload capabilities

*As mentioned above, we will discuss where Vercel breaks down and why as our backends become more sophisticated.

The 🚧 Advanced Builds today will incorporate elements of Session 2 into building both an advanced backend and an advanced frontend.

- Backend features: LLM, `.csv` and `.pdf` upload, chunking utilities
- Frontend features: calls your backend, deployed to Vercel

## 🤩 **For Fun**

- Strategies for chunking documents can be visualized with [ChunkViz](https://chunkviz.up.railway.app/)
