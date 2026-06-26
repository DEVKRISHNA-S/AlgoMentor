# app/main.py

import streamlit as st

from ui.sidebar import render_sidebar
from ui.chat import render_chat
from ui.problem_solver import render_problem_solver
from ui.code_review import render_code_review
from ui.knowledge_base import render_knowledge_base


st.set_page_config(
    page_title="AlgoMentor",
    page_icon="🧠"
)

if "messages" not in st.session_state:
    st.session_state.messages = []


mode = render_sidebar()

st.title("AlgoMentor")

st.write(
    "Learn DSA through guided hints, code reviews, and problem-solving."
)




if mode == "Chat":
    render_chat()

elif mode == "Problem Solver":
    render_problem_solver()

elif mode == "Code Review":
    render_code_review()

elif mode == "Knowledge Base":
    render_knowledge_base()