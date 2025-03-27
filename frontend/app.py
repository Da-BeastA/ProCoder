import streamlit as st
import requests

st.title("📚 Code Tutor")

# User options
st.write("### Help me to:")
option = st.radio(
    "",
    ["Understand", "Comment", "Debug", "Improve"],
    horizontal=True,
)

# Topic input
topic = st.text_input("Topic (Optional):")

# Code input
code_input = st.text_area("My Code:")

# Analyze button
if st.button("Analyze Code"):
    if not code_input.strip():
        st.warning("Please enter some code before analyzing.")
    else:
        # Send request to FastAPI backend
        response = requests.post(
            "http://127.0.0.1:8000/analyze/",
            json={"code": f"{option} the following code on {topic}:\n\n{code_input}"}
        )
        if response.status_code == 200:
            st.subheader("Analysis:")
            st.write(response.json()["analysis"])
        else:
            st.error("Error: Could not process the code analysis.")
