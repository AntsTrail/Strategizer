def run(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b


metadata = {
    "name": "summation",
    "description": "Adds two numbers.",
    "parameters": {"a": "First number (float)", "b": "Second number (float)"},
    "returns": "float",
}
