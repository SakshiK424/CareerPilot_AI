import streamlit as st

from database.schema import initialize_database
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

initialize_database()

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


st.title("🚀 CareerPilot AI")

st.markdown("""
## Your Personal AI Career Guidance Platform

This platform helps you:

- ✅ Analyze Resume
- ✅ Find Skill Gaps
- ✅ Explore Market Trends
- ✅ Generate Career Roadmaps
- ✅ Chat with an AI Career Mentor
- ✅ Get Personalized Career Advice
""")

st.success("Use the sidebar to explore all AI tools.")