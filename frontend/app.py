import streamlit as st
import requests

st.title("ProCoder: Mistral-Powered Code Assistant")

# Code input field
code_input = st.text_area("Enter your code here:")

if st.button("Analyze Code"):
    response = requests.post("http://127.0.0.1:8000/analyze/", json={"code": code_input})
    if response.status_code == 200:
        st.subheader("Analysis:")
        st.write(response.json()["analysis"])
    else:
        st.error("Error: Could not process the code analysis.")
