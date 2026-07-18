import streamlit as st

from services.market_service import generate_market_analysis

st.set_page_config(
    page_title="Market Analysis",
    page_icon="📈"
)

st.title("📈 AI Market Analysis")

st.write("Analyze the current market trends for your desired career.")

target_role = st.text_input(
    "Enter Target Career",
    placeholder="Example: AI Engineer"
)

if st.button("Analyze Market"):

    if target_role.strip() == "":
        st.warning("Please enter a target career.")
    else:

        with st.spinner("Analyzing Market Trends..."):

            report = generate_market_analysis(target_role)

        st.subheader("📊 Market Analysis Report")

        st.markdown(report)