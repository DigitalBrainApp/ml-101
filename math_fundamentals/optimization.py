"""Optimization module.

Defines some simple optimization algorithms.

Let's go through the different inputs to the optimization algorithm:

- `function`: The function that needs to be optimized
- `starting_point`: Initial solution which the algorithms iteratively updates
- `steps`: Number of times to perform the update

Additionally, each algorithm might contain additional arguments that change its internals.
"""

from typing import Callable

import numpy as np


def hill_climbing(
    function: Callable[[float], float],
    starting_point: float,
    steps: int = 100,
    scale: float = 1,
) -> float:
    """Hill climbing optimization algorithm.

    Iteratively:
    - Select a random point close to the current point
    - Evaluate the function at that point
    - If better, set that point as the current point

    Terminate after the specified number of steps (default 100).

    The argument `scale` determines how far away from the current point to select candidates from.
    """
    # Evaluate the current solution (the starting point)
    current = starting_point
    current_value = function(starting_point)

    for _ in range(steps):
        # Pick a candidate some random distance away from the current solution
        candidate = np.random.normal(loc=current, scale=scale)
        candidate_value = function(candidate)

        # Check if the candidate is better than the current solution
        if candidate_value > current_value:
            current = candidate
            current_value = candidate_value

    return current


def gradient_ascent(
    function: Callable[[float], float],
    starting_point: float,
    steps: int = 100,
    step_size: float = 0.01,
    epsilon: float = 1e-5,
) -> float:
    """Gradient ascent optimization algorithm.

    Iteratively:
    - Calculate the slope at the current point
    - Move upwards according to the slope and proportional to how steep the slope is

    Terminate after the specified number of steps (default 100).

    The argument `step_size` determines how big the update should be on each iteration.
    """
    def slope(
        function: Callable[[float], float],
        current: float,
        epsilon: float,
    ) -> float:
        right_side = function(current + epsilon)
        left_side = function(current - epsilon)
        vertical_difference = right_side - left_side
        horizontal_difference = 2 * epsilon
        return vertical_difference / horizontal_difference

    # Start from the starting point
    current = starting_point

    for _ in range(steps):
        # Calculate the slope at the current point
        current_slope = slope(function, current, epsilon=epsilon)

        # Update the current point according to the slope
        current = current + step_size * current_slope

    return current
