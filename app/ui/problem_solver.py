# app/ui/problem_solver.py

from llm.ollama_client import ask_model
import streamlit as st


def render_problem_solver():

    st.header("Problem Solver")

    problem = st.text_area(
        "Paste LeetCode / Codeforces Problem",
        height=250
    )

    if st.button("Analyze Problem"):

        if problem:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": problem
                }
            )

            answer = ask_model(
                st.session_state.messages,
                "Problem Solver"
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()