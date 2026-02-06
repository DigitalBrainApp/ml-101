# Math Fundamentals for Machine Learning

Interactive journey to understand the mathematical foundations of machine learning.

## Getting Started

To run the interactive visualizations, use the following command from the project root:

```bash
uv run streamlit run math_fundamentals/visualizations.py
```

This will launch a Streamlit app in your browser with multiple pages for different topics.

## Topics

### 1. What is a function?

**Page:**  [Function Visualizer](http://localhost:8501/functions)

Start here to understand the concept of functions. A function `f` takes an input (`x`) and produces an output (`f(x)`).

**What to explore:**
- Select different functions from the sidebar (`f`, `square`, `sqrt`, `cosine`)
- Observe how the input values map to output values
- Notice the different shapes and behaviors of different functions
- Read the function documentation to understand what each one does
- Explore the [code](./functions.py), can you understand the definitions?

### 2. What does it mean to "optimize" a function?

**Page:** [Optimization Visualizer](http://localhost:8501/optimization)

Optimization means finding the input value that produces the maximum (or minimum) output value.

**What to explore:**
- Look at the complex function with multiple peaks and valleys
- Identify the global maximum (highest peak - green marker)
- Identify the local maximum (smaller peak - orange marker)

**Key concepts:**
- Global vs. local optima

### 3. Simple optimization: Hill Climbing

**Page:** [Optimization Visualizer](http://localhost:8501/optimization)

Hill climbing is a simple optimization algorithm that explores randomly around the current point.

**What to try:**
1. Select `hill_climbing` from the optimizer dropdown
2. Set a starting point (try `0.0` first)
3. Adjust the `scale` parameter (controls how far it searches)
4. Click `Run Optimization`
5. Use the replay slider to watch the optimization process step-by-step

**Experiments:**
- Try different starting points (`-10`, `0`, `10`)
- Does it always find the global maximum?
- Can you make it get stuck on the local maximum instead?
- What happens with different scale values?
- Can it escape local maxima?

**Key concepts:**
- Local optima problem

### 4. Optimizing with Calculus: Gradient Ascent

**Page:** 🎯 [Optimization Visualizer](http://localhost:8501/optimization)

Gradient ascent uses derivatives to climb uphill efficiently, following the steepest direction.

Derivatives are a concept from calculus we'll touch on in the next section. For now, you can think of it as the _slope_ of the function.

**What to try:**
1. Select `gradient_ascent` from the optimizer dropdown
2. Set a starting point
3. Adjust `step_size` (how far to move in each step)
4. Click `Run Optimization`
5. Watch how it follows the gradient uphill

**Experiments:**
- Compare gradient ascent vs. hill climbing from the same starting point
- Try different step sizes (`0.01` vs. `0.1` vs. `1.0`)
- What happens if the step size is too large?
- Does gradient ascent get stuck in local maxima?

**Key concepts:**
- Gradient = direction of steepest ascent
- Derivative = slope
- Step size

### 5. (Optional) What is a derivative?

**Concept:** A derivative measures how much a function changes when you change the input slightly. It's the slope of the function at a specific point.

**In the visualizer:**
- Steep slopes = large derivative
- Flat areas = derivative near zero
- The derivative points "uphill" toward higher values

There's many resources on this in the internet, and it's not exactly required to get the point. But you may find [these illustrations](https://allisonhorst.com/derivatives-series) cute.

## Implementation Details

In case you're interested in the code that defines some of these, I've tried to be pretty thorough in documentation.

- **Functions:** Defined in [`math_fundamentals/functions.py`](./functions.py)
- **Optimizers:** Defined in [`math_fundamentals/optimization.py`](./optimization.py)

I would not look at the code for the visualizations, that one is gnarlier.

## Application to Machine Learning

In Machine Learning when training neural networks, we define _loss functions_ (how bad the model is) and we try to minimize them (minimizing badness == maximizing goodness!)

The main algorithm used is gradient descent, though it has a few adaptations to be able to escape local minima and reach better solutions faster.

In this module, we worked with single variable functions. When optimizing neural networks we are optimizing many variables which interact in complex ways.

![Complex loss landscape of neural nets](./images/loss_landscape.png)
*A neural network's loss landscape (2D slice shown in 3D). Like the single-variable function we optimized, it has peaks and valleys—but with thousands of dimensions instead of just one! Red/high = bad (high loss), blue/low = good (low loss). Gradient descent navigates this landscape to find the lowest valleys.*
