# app/main.py

import streamlit as st
from llm.ollama_client import ask_model

st.set_page_config(
    page_title="DSA Mentor",
    page_icon="🧠"
)

st.title("DSA Mentor")
st.write("Ask DSA, LeetCode and Codeforces questions.")

question = st.text_area(
    "Your Question",
    height=150
)

if st.button("Ask Mentor"):

    if question:

        with st.spinner("Thinking..."):

            answer = ask_model(question)

        st.markdown(answer)