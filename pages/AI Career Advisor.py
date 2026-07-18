import streamlit as st

from services.pdf_service import extract_text_from_pdf
from services.graph_service import run_career_graph
from services.pdf_report_service import create_pdf

st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Advisor (LangGraph Powered)")

st.write(
    "Upload your resume and select your target career. "
    "Our AI agents will work together to generate a complete career report."
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

target_role = st.selectbox(
    "Select Your Target Career",
    [
        "AI Engineer",
        "Data Scientist",
        "Machine Learning Engineer",
        "Software Engineer",
        "Frontend Developer",
        "Backend Developer",
        "Full Stack Developer",
        "Cloud Engineer",
        "Cyber Security Engineer",
        "DevOps Engineer",
        "Data Analyst",
        "Business Analyst",
        "Android Developer",
        "UI/UX Designer"
    ]
)

if uploaded_file and target_role:

    resume_text = extract_text_from_pdf(uploaded_file)

    if st.button("Generate Complete Career Report"):

        with st.spinner("Running AI Agents..."):

            result = run_career_graph(
                resume_text,
                target_role
            )

            # Generate PDF
            create_pdf(
                "career_report.pdf",
                result["resume_report"],
                "",   # Skill Gap not in LangGraph yet
                result["market_report"],
                result["roadmap_report"],
            )

        st.success("✅ Career Report Generated Successfully!")

        st.header("📄 Resume Analysis")
        st.markdown(result["resume_report"])

        st.header("📈 Market Analysis")
        st.markdown(result["market_report"])

        st.header("🗺️ Career Roadmap")
        st.markdown(result["roadmap_report"])

        # Download Button
        with open("career_report.pdf", "rb") as pdf_file:
            st.download_button(
                label="📥 Download Career Report (PDF)",
                data=pdf_file,
                file_name="CareerPilot_AI_Report.pdf",
                mime="application/pdf",
            )