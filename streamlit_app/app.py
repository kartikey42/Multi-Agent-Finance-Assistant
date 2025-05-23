# -----------------------------
import streamlit as st
import requests

st.title("Morning Market Brief")

if st.button("Get Brief"):
    r = requests.get("http://localhost:8000/brief")
    st.write(r.json()["text"])