import streamlit as st
import pandas as pd

def load_users():
    users_df = pd.read_csv("users.csv")
    users = {}
    for _, row in users_df.iterrows():
        users[row['username']] = {'password': row['password'], 'role': row['role']}
    return users

users = load_users()

st.set_page_config(page_title="Login", layout="wide")
st.title("🔐 Employee Attendance System")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""

if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username]['password'] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = users[username]['role']
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password")
else:
    st.write("✅ Go to your dashboard using the left sidebar navigation.")
    st.sidebar.success(f"Logged in as: {st.session_state.username} ({st.session_state.role})")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.experimental_rerun()
