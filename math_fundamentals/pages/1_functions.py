"""Streamlit page for visualizing functions.py."""

import inspect
import textwrap

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import functions

# Get all functions from the functions module
all_functions = {
    name: obj for name, obj in inspect.getmembers(functions)
    if inspect.isfunction(obj) and obj.__module__ == "functions"
}

# Page configuration
st.set_page_config(page_title="ML 101 - Function Visualizer", page_icon="🔍", layout="wide")

# Visualization config
x_min = -10
x_max = +10
num_points = 10001

# Generate x values
x_values = np.linspace(x_min, x_max, num_points)

# Sidebar for controls
with st.sidebar:
    st.header("Function picker")
    st.markdown("Definitions available in [`math_fundamentals/functions.py`](https://github.com/DigitalBrainApp/ml-101/blob/main/math_fundamentals/functions.py).")

    # Function selector
    function_names = sorted(all_functions.keys())
    selected_function_name = st.selectbox(
        "Choose a function",
        function_names,
        index=0
    )

    # Get the selected function and its metadata
    selected_function = all_functions[selected_function_name]
    function_name = selected_function.__name__
    function_doc = selected_function.__doc__ or "No documentation available."

    # Calculate y values using the selected function
    y_values = [selected_function(x) for x in x_values]

    # Display some statistics
    col1, col2 = st.columns(2)
    valid_ys = [y for y in y_values if not np.isnan(y)]
    with col1:
        st.metric(f"Minimum {function_name}(x)", f"{min(valid_ys):.2f}")
    with col2:
        st.metric(f"Maximum {function_name}(x)", f"{max(valid_ys):.2f}")

# Create the plot
fig = go.Figure()

# Add the function line
fig.add_trace(go.Scatter(
    x=x_values,
    y=y_values,
    mode="lines",
    name=f"{function_name}(x)",
    line=dict(color="#FF6B6B", width=3)
))

# Update layout for better appearance
fig.update_layout(
    title=f"Function {function_name}(x)",
    xaxis_title="x",
    yaxis_title=f"{function_name}(x)",
    hovermode="x unified",
    template="plotly_white",
    height=600,
    font=dict(size=14)
)

# Information section
with st.expander(f"ℹ️ About the function **{function_name}(x)**"):
    st.markdown(textwrap.dedent("    " + function_doc))

# Display the plot
st.plotly_chart(fig, width="stretch")
