# sidebar.py
import streamlit as st

def render_sidebar():
    with st.sidebar:
        if st.button("🔄 새로 시작"):
            st.session_state.clear()
            st.rerun()
