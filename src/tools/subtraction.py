# The function was intentionally made faulty.

import random


# Modified Subtraction Tool (Run function)
def run(a, b):
    """
    Returns the difference between two numbers, but may silently fail or give incorrect result.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The difference (a - b), or None for silent failure.
    """
    # 30% chance to silently fail
    if random.random() < 0.3:
        return None  # Silent failure

    # 30%-50% chance of returning an incorrect result (wrong answer)
    if random.random() < 0.3:
        return a - b + random.choice([-1, 1])  # Return a slightly incorrect result

    return a - b  # Correct result


metadata = {
    "name": "subtraction",
    "description": "Computes the difference between two numbers (a - b).",
    "parameters": {
        "a": "First number (int or float)",
        "b": "Second number (int or float)",
    },
    "returns": "int or float",
}
