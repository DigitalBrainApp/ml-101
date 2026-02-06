"""This module implements simple functions.

Let's go through the different pieces involved in a function definition like:

def f(x: float) -> float:
    ....

- `def`         is a keyword that states we're about to define a new function
- `f`      is the name of that function, it can be now used elsewhere to reuse this code
- `x: float`    is the specification of the input (named `x`) which is a number (float)
- `-> float`    is the specification that the output of this function will be a number (float)

The code indented within the function definition corresponds to instructions to calculate the result.
"""

def f(x: float) -> float:
    """This function returns double its input.

    Examples:
    - `f(5)`  => 10
    - `f(10)` => 20
    """
    return x * 2  # Multiplies the input by two


def square(x: float) -> float:
    """This function implements the square of a number, equivalent to multiplying the number by itself.

    This is the inverse of the square root function!

    Examples:
    - `square(2)`   => 4
    - `square(3)`   => 9
    - `square(10)`  => 100
    """
    return x * x  # Multiplies the input by itself


def sqrt(x: float) -> float:
    """This function implements the square root of a number.

    This is the inverse of the square function!

    Examples:
    - `sqrt(4)`     => 2
    - `sqrt(9)`     => 3
    - `sqrt(100)`   => 10
    """
    import numpy as np  # This function implementation is available from a library!
    return np.sqrt(x)


def cosine(x: float) -> float:
    """This function implements the periodic function cosine.

    You can read more on cosine on [Wikipedia](https://en.wikipedia.org/wiki/Sine_and_cosine).

    Examples:
    - `cosine(0)`       => 1.0
    - `cosine(π / 2)`   => 0.0
    - `cosine(π)`       => -1.0
    - `cosine(2 * π)`   => 0.0
    """
    import numpy as np  # This function implementation is available from a library!
    return np.cos(x)
