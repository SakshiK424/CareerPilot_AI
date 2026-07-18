from services.career_service import analyze_resume
import streamlit as st
from services.pdf_service import extract_text_from_pdf

st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📄"
)

st.title("📄 Resume Analysis")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Resume")

    st.text_area(
        "Resume Content",
        resume_text,
        height=400
    )
    if st.button("Analyze Resume"):

        with st.spinner("Analyzing your resume..."):

           analysis = analyze_resume(resume_text)

        st.subheader("📊 AI Resume Analysis")

        st.markdown(analysis)