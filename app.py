import streamlit as st
from PyPDF2 import PdfReader

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    pdf = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    st.success("Resume Uploaded Successfully!")

    st.subheader("Resume Content")

    st.text_area(
        "Extracted Text",
        resume_text,
        height=300
    )