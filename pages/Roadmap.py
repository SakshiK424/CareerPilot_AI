import streamlit as st

from services.pdf_service import extract_text_from_pdf
from services.roadmap_service import generate_career_roadmap

st.set_page_config(
    page_title="Career Roadmap",
    page_icon="🗺️"
)

st.title("🗺️ AI Career Roadmap")

st.write("Generate a personalized career roadmap based on your resume and target role.")

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

    with st.expander("View Resume"):
        st.text_area(
            "Resume Text",
            resume_text,
            height=300
        )

    if st.button("Generate Roadmap"):

        with st.spinner("Creating your roadmap..."):

            roadmap = generate_career_roadmap(
                resume_text,
                target_role
            )

        st.subheader("🛣️ Personalized Career Roadmap")

        st.markdown(roadmap)