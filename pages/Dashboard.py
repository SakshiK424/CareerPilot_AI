from services.chart_service import salary_chart, skill_chart
import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 CareerPilot AI Dashboard")

st.write("Welcome to your AI Career Guidance Platform!")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Resume Score", "85/100")

with col2:
    st.metric("ATS Score", "82%")

with col3:
    st.metric("Career Match", "88%")

with col4:
    st.metric("Skills Found", "12")

st.markdown("---")

st.subheader("🚀 Quick Features")

col1, col2 = st.columns(2)

with col1:
    st.info("📄 Resume Analysis")
    st.info("🎯 Skill Gap Analysis")

with col2:
    st.info("🗺️ Career Roadmap")
    st.info("📈 Market Analysis")

    st.markdown("---")

st.subheader("📊 Career Analytics")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        salary_chart(),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        skill_chart(),
        use_container_width=True
    )