from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <h2>🔥 Hot Mess Coach</h2>
    <form action="/chat" method="post">
        <p>Your message:</p>
        <textarea name="user_message" rows="4" cols="50">I feel like a hot mess today...</textarea><br><br>
        <button type="submit">Coach me</button>
    </form>
    """

@app.post("/chat", response_class=HTMLResponse)
def chat(user_message: str = Form(...)):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a supportive mental coach who helps overwhelmed people feel calmer."},
            {"role": "user", "content": user_message},
        ]
    )

    coach_reply = response.choices[0].message.content

    return f"""
    <h2>🔥 Hot Mess Coach Says</h2>
    <div style="white-space: pre-wrap; border: 1px solid #ccc; padding: 12px; border-radius: 8px;">
        {coach_reply}
    </div>
    <br><a href="/">⬅ Back</a>
    """

#uv run uvicorn STEP2_app_llm_html:app --reload --host 0.0.0.0 --port 8000