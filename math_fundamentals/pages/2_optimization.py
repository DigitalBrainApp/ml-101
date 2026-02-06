"""Streamlit page for visualizing optimization.py."""

import inspect
import textwrap

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import optimization

# Page configuration
st.set_page_config(page_title="ML 101 - Optimization Visualizer", page_icon="🔍", layout="wide")

# Get all optimizers from the optimization module
all_optimizers = {
    name: obj for name, obj in inspect.getmembers(optimization)
    if inspect.isfunction(obj) and obj.__module__ == "optimization"
}


def f(x: float) -> float:
    """Non-convex function with multiple local minima and maxima."""
    return - (x * np.sin(x / 2 - 3) + 0.15 * x ** 2 - 20 * np.cos(0.5 * (x / 2 - 2)))

# Sidebar for optimizer controls
with st.sidebar:
    st.header("Optimization Settings")

    # Optimizer selector
    optimizer_names = reversed(sorted(all_optimizers.keys()))
    selected_optimizer_name = st.selectbox(
        "Choose optimizer",
        optimizer_names,
        index=0
    )
    st.markdown("Definitions available in [`math_fundamentals/optimization.py`](https://github.com/DigitalBrainApp/ml-101/blob/main/math_fundamentals/optimization.py).")
    selected_optimizer = all_optimizers[selected_optimizer_name]

    # Common parameters
    starting_point = st.slider("Starting point", -20.0, 20.0, 0.0, 0.1)
    total_iterations = 100

    # Optimizer-specific parameters
    if selected_optimizer_name == "hill_climbing":
        scale = st.slider("Scale", 0.1, 5.0, 1.0, 0.1)
        optimizer_params = {"scale": scale}
    elif selected_optimizer_name == "gradient_ascent":
        step_size = st.slider("Step size", 0.001, 1.0, 0.01, 0.001)
        optimizer_params = {"step_size": step_size}
    else:
        optimizer_params = {}

    # Run button
    run_optimization = st.button("Run Optimization", type="primary", use_container_width=True)

# Initialize session state for trajectory
if "trajectory" not in st.session_state:
    st.session_state.trajectory = None

# Run optimization when button is clicked
if run_optimization:
    trajectory = [starting_point]
    current_point = starting_point

    # Run optimizer repeatedly with steps=1
    for _ in range(total_iterations):
        next_point = selected_optimizer(
            function=f,
            starting_point=current_point,
            steps=1,
            **optimizer_params
        )
        trajectory.append(next_point)
        current_point = next_point

    # Store trajectory in session state
    st.session_state.trajectory = trajectory

# Visualization config
x_min = -20
x_max = 20
num_points = 10001

# Generate x values
x_values = np.linspace(x_min, x_max, num_points)

# Calculate y values using the selected function
y_values = [f(x) for x in x_values]

# Information section about the optimizer
optimizer_doc = selected_optimizer.__doc__ or "No documentation available."
with st.expander(f"ℹ️ About the optimizer **{selected_optimizer_name}**"):
    st.markdown(textwrap.dedent("    " + optimizer_doc))

# Create placeholder for the plot
plot_placeholder = st.empty()

# Replay slider (outside the plot so layout doesn't shift)
current_iteration = 0
if st.session_state.trajectory is not None:
    current_iteration = st.slider(
        "Replay iteration",
        0,
        len(st.session_state.trajectory) - 1,
        len(st.session_state.trajectory) - 1,
        1
    )

# Create the plot
fig = go.Figure()

# Add the function line
fig.add_trace(go.Scatter(
    x=x_values,
    y=y_values,
    mode="lines",
    name="f(x)",
    line=dict(color="#FF6B6B", width=3)
))

# Maxima coordinates (calculated using scipy optimization)
global_max_x = 3.489020
global_max_y = f(global_max_x)
local_max_x = -16.201647
local_max_y = f(local_max_x)

# Add global maximum marker
fig.add_trace(go.Scatter(
    x=[global_max_x],
    y=[global_max_y],
    mode="markers+text",
    name="Global Maximum",
    marker=dict(color="#2ECC71", size=15, symbol="circle", line=dict(color="white", width=2)),
    text=["Global Max"],
    textposition="top center",
    textfont=dict(size=12, color="#2ECC71", family="Arial Black")
))

# Add local maximum marker
fig.add_trace(go.Scatter(
    x=[local_max_x],
    y=[local_max_y],
    mode="markers+text",
    name="Local Maximum",
    marker=dict(color="#F39C12", size=15, symbol="circle", line=dict(color="white", width=2)),
    text=["Local Max"],
    textposition="top center",
    textfont=dict(size=12, color="#F39C12", family="Arial Black")
))

# Add trajectory visualization if optimization has been run
if st.session_state.trajectory is not None:
    # Get trajectory up to current iteration
    trajectory_x = st.session_state.trajectory[:current_iteration + 1]
    trajectory_y = [f(x) for x in trajectory_x]

    # Add path of visited points
    fig.add_trace(go.Scatter(
        x=trajectory_x,
        y=trajectory_y,
        mode="lines+markers",
        name="Optimization Path",
        line=dict(color="#3498DB", width=2),
        marker=dict(size=6, color="#3498DB", symbol="circle")
    ))

    # Find and mark the current best point
    best_idx = np.argmax(trajectory_y)
    best_x = trajectory_x[best_idx]
    best_y = trajectory_y[best_idx]

    fig.add_trace(go.Scatter(
        x=[best_x],
        y=[best_y],
        mode="markers+text",
        name="Current Best",
        marker=dict(color="#9B59B6", size=20, symbol="star", line=dict(color="white", width=2)),
        text=["Best"],
        textposition="bottom center",
        textfont=dict(size=12, color="#9B59B6", family="Arial Black")
    ))

# Update layout for better appearance
fig.update_layout(
    title=f"Function f(x)",
    xaxis_title="x",
    yaxis_title="f(x)",
    hovermode="x unified",
    template="plotly_white",
    height=600,
    font=dict(size=14)
)

# Display the plot in the placeholder
plot_placeholder.plotly_chart(fig, use_container_width=True)
