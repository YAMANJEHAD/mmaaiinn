import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="لوحة المدير", layout="wide")
st.title("🧑‍💼 لوحة المدير")

logs = pd.read_csv("logs.csv", names=["الاسم", "الحالة", "الوقت"])

search_name = st.text_input("🔍 ابحث بالاسم")
if search_name:
    logs = logs[logs["الاسم"].str.contains(search_name, case=False)]

st.dataframe(logs)

if st.button("📥 تحميل البيانات"):
    logs.to_excel("سجلات_الحضور.xlsx", index=False)
    with open("سجلات_الحضور.xlsx", "rb") as f: 
        st.download_button("⬇️ تحميل Excel", f, "سجلات_الحضور.xlsx")
