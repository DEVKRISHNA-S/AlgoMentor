# app/ui/code_review.py

from llm.ollama_client import ask_model
import streamlit as st


def render_code_review():

    st.header("Code Review")

    code = st.text_area(
        "Paste Your Code",
        height=250
    )

    if st.button("Review Code"):

        if code:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": code
                }
            )

            answer = ask_model(
                st.session_state.messages,
                "Code Review"
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()