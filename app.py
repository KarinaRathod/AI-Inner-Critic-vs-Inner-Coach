import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import datetime

# -----------------------------
# LOAD ENV
# -----------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="Inner Critic vs Coach", layout="wide")
st.title("🧠⚖️ Inner Critic vs Inner Coach")
st.caption("See both sides of your thoughts")

# -----------------------------
# SESSION STATE
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# INPUT
# -----------------------------
thought = st.text_area("💭 What’s on your mind?", height=150)

# -----------------------------
# GENERATE
# -----------------------------
if st.button("🔍 Analyze Thought"):

    if not thought.strip():
        st.warning("⚠️ Please enter your thought")
        st.stop()

    with st.spinner("🧠 Thinking deeply..."):

        prompt = f"""
        A user has this thought:
        "{thought}"

        Generate three sections:

        1. Inner Critic:
        - Show negative self-talk
        - Realistic but not abusive

        2. Inner Coach:
        - Supportive and rational
        - Reframe the situation logically

        3. Balanced Insight:
        - Combine both views
        - Give 1 actionable step

        Keep it deep, meaningful, and concise.
        """

        response = model.generate_content(prompt)
        result = response.text

        # Save
        st.session_state.history.append({
            "time": str(datetime.datetime.now()),
            "thought": thought,
            "result": result
        })

        # -----------------------------
        # DISPLAY
        # -----------------------------
        st.subheader("😈 Inner Critic")
        critic = result.split("Inner Coach")[0]
        st.error(critic)

        st.subheader("😇 Inner Coach")
        try:
            coach = result.split("Inner Coach")[1].split("Balanced Insight")[0]
        except:
            coach = "Could not parse"
        st.success(coach)

        st.subheader("⚖️ Balanced Insight")
        try:
            insight = result.split("Balanced Insight")[1]
        except:
            insight = result
        st.info(insight)

# -----------------------------
# HISTORY
# -----------------------------
if st.session_state.history:
    st.subheader("📜 Past Reflections")

    for item in reversed(st.session_state.history[-5:]):
        st.write(f"🕒 {item['time']}")
        st.write(f"💭 {item['thought']}")
        st.write(item['result'])
        st.divider()