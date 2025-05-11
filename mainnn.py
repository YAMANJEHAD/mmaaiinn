import streamlit as st
import pandas as pd
from datetime import datetime
import os

# إعداد الصفحة
st.set_page_config(page_title="Attendance System", layout="wide")

# تخصيص التصميم
st.markdown("""
<style>
.main {
    background-color: #f4f4f4;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# عنوان الصفحة
st.title("📋 نظام تسجيل الحضور")

# تحميل بيانات المستخدمين
@st.cache_data
def load_users():
    return pd.read_csv("users.csv")

users_df = load_users()

# حقل اسم المستخدم وكلمة المرور
username = st.text_input("👤 اسم المستخدم")
password = st.text_input("🔐 كلمة المرور", type="password")

if st.button("تسجيل الدخول"):
    # التحقق من المستخدم
    user = users_df[(users_df['username'] == username) & (users_df['password'] == password)]
    if not user.empty:
        role = user.iloc[0]["role"]
        if role == "supervisor":
            st.switch_page("pages/3_Supervisor_Dashboard.py")
        elif role == "technician":
            st.switch_page("pages/2_Technician_Dashboard.py")
        else:
            st.switch_page("pages/1_Employee_Dashboard.py")
    else:
        st.error("❌ معلومات الدخول غير صحيحة")
