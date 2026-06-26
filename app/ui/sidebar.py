# app/ui/sidebar.py

import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("AlgoMentor")

        mode = st.radio(
            "Choose Mode",
            [
                "Chat",
                "Problem Solver",
                "Code Review",
                "Knowledge Base"
            ]
        )

        st.divider()

        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    return mode