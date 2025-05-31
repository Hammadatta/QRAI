# main.py
import streamlit as st

st.set_page_config(page_title="Qorvex AI", layout="wide")

st.title("Qorvex AI Risk Monitor 🚀")
st.markdown("Monitor prompt injection, plugin abuse, and risky inputs.")

# Test input field
user_prompt = st.text_input("🔍 Enter a user prompt to analyze:")

# Simple detector logic
if user_prompt:
    if any(phrase in user_prompt.lower() for phrase in ["ignore", "you are now", "act as", "jailbreak", "###"]):
        st.error("⚠️ Prompt Injection Detected!")
    else:
        st.success("✅ Prompt is clean.")

