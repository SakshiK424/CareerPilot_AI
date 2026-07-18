import streamlit as st

from services.pdf_service import extract_text_from_pdf
from services.skill_gap_service import analyze_skill_gap

st.set_page_config(
    page_title="Skill Gap Analysis",
    page_icon="🎯"
)

st.title("🎯 Skill Gap Analysis")

st.write("Upload your resume and select your target career.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

target_role = st.text_input(
    "Target Career",
    placeholder="Example: AI Engineer"
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    with st.expander("View Extracted Resume"):
        st.text_area(
            "Resume",
            resume_text,
            height=300
        )

    if st.button("Analyze Skill Gap"):

        with st.spinner("Analyzing..."):

            result = analyze_skill_gap(
                resume_text,
                target_role
            )

        st.subheader("Skill Gap Report")

        st.markdown(result)