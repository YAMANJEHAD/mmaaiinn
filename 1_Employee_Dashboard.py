import streamlit as st
from datetime import datetime

# إعداد الصفحة
st.set_page_config(page_title="لوحة الموظف", layout="wide")
st.title("👨‍💼 لوحة الموظف")

employee_name = st.text_input("الرجاء إدخال اسمك الكامل", max_chars=30)

if st.button("📥 تسجيل الدخول"):
    with open("logs.csv", "a", encoding="utf-8") as f:
        f.write(f"{employee_name},دخول,{datetime.now()}\n")
    st.success("✅ تم تسجيل الدخول بنجاح")

if st.button("📤 تسجيل الخروج"):
    with open("logs.csv", "a", encoding="utf-8") as f:
        f.write(f"{employee_name},خروج,{datetime.now()}\n")
    st.success("✅ تم تسجيل الخروج بنجاح")
