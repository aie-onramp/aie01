<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading"> 👋 Hot Mess Coach — Simple LLM App Variants</h1>

This repo contains a few minimal FastAPI/Streamlit examples that progress from a basic HTML page to an LLM-backed UI with document upload. Keep the vibe, keep it simple.

Our deployed Vercel applications are here: 
1. https://aim-hot-mess-coach.vercel.app/
   with GitHub repo available here: https://github.com/katgaw/AIM-hot-mess-coach
2. https://aim-hot-mess-coach-upload.vercel.app/
    with GitHub repo available here: https://github.com/katgaw/AIM-hot-mess-coach-upload
    
### Quick Start

```bash
uv init
uv add fastapi "uvicorn[standard]" python-dotenv openai streamlit
uv sync
export OPENAI_API_KEY=sk-...   # required for LLM variants
```

### App Variants (FastAPI + Streamlit)

- app_html.py → `backend/STEP0_app_html.py`
  - Simple FastAPI app wrapped in HTML so you can test quickly.
  - Run:
    ```bash
    uv run uvicorn backend.STEP0_app_html:app --reload --host 0.0.0.0 --port 8000
    ```
  - Open `http://127.0.0.1:8000`

- app_llm.py → `backend/STEP1_app_llm.py`
  - Simple LLM backend (no UI). Exposes `POST /chat`.
  - Run:
    ```bash
    uv run uvicorn backend.STEP1_app_llm:app --reload --host 0.0.0.0 --port 8000
    ```
  - Try Swagger: `http://127.0.0.1:8000/docs`

- app_llm_html.py → `backend/STEP2_app_llm_html.py`
  - LLM backend wrapped in a minimal HTML UI.
  - Run:
    ```bash
    uv run uvicorn backend.STEP2_app_llm_html:app --reload --host 0.0.0.0 --port 8000
    ```
  - Open `http://127.0.0.1:8000`

- llm_st.py → `backend/STEP3_app_llm_st.py`
  - Streamlit UI for a nicer chat experience.
  - Run:
    ```bash
    uv run streamlit run backend/STEP3_app_llm_st.py
    ```

- llm_st_doc.py → `backend/STEP4_app_llm_st_doc.py`
  - Streamlit UI + document upload (PDF/CSV) that is injected as context for analysis.
  - Run:
    ```bash
    uv run streamlit run backend/STEP4_app_llm_st_doc.py
    ```
  - For PDFs/CSVs:
    ```bash
    uv add PyPDF2 pandas
    ```
