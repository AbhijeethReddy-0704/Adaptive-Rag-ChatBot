"""
Home page - Simple login for local development.
"""

import streamlit as st

st.set_page_config(page_title="LangGraph Chat - Login", layout="wide")

st.title("🔐 Welcome to LangGraph Assistant")

# Initialize session
if "session_id" not in st.session_state:
    st.session_state["session_id"] = None

if "username" not in st.session_state:
    st.session_state["username"] = None

# Login form
with st.form("auth_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

    if submit:
        if not username or not password:
            st.error("Username and password required.")
        else:
            # Simple local authentication
            st.session_state["session_id"] = f"session_{username}"
            st.session_state["username"] = username
            st.session_state["jwt_token"] = "local_token"
            st.success("Login successful!")
            st.switch_page("pages/Chat.py")