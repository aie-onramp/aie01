import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Hot Mess Coach", page_icon="🔥")

st.title("🔥 Hot Mess Coach")
st.write("Your supportive mini mental coach powered by gpt-4o-mini.")

user_msg = st.text_area("How are you feeling today?", "I feel like a hot mess today...")

if st.button("Coach me"):
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a supportive mental coach who helps overwhelmed people feel calmer."},
                {"role": "user", "content": user_msg},
            ],
        )
        reply = response.choices[0].message.content
        st.subheader("💬 Coach says:")
        st.write(reply)

##uv run streamlit run STEP3_app_llm_st.py