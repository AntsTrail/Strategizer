import math


def run(a):
    """
    Returns the square root of the given number.

    Parameters:
    a (int or float): The number.

    Returns:
    float: The square root of the number.

    Raises:
    ValueError: If a is negative.
    """
    if a >= 0:
        return math.sqrt(a)
    else:
        raise ValueError("Cannot take square root of a negative number")


metadata = {
    "name": "square_root",
    "description": "Computes the square root of a non-negative number.",
    "parameters": {
        "a": "The number (int or float) for which to compute the square root."
    },
    "returns": "float",
}
