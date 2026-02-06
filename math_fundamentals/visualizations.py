"""Main streamlit entry point."""

import streamlit as st

st.set_page_config(
    page_title="ML 101 - Math fundamentals visualizations",
    page_icon="🔍",
)

st.header("ML 101 - Math fundamentals visualizations")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Supplementary material to [Math fundamentals](https://github.com/DigitalBrainApp/ml-101/blob/main/math_fundamentals/).

    The streamlit server is now running on your terminal.

    If you wish to stop it at any time, go back to your terminal and press `Ctrl + C`.
"""
)
