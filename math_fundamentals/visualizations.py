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

    Follow along the course material on the [github page](https://github.com/DigitalBrainApp/ml-101/tree/main/math_fundamentals),
    it will provide you with links to different parts of the streamlit application, which will work as long as you are running the server.
"""
)
