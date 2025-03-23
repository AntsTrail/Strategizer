import math
from langchain.tools import Tool

# Define the tool class that matches the new format
class SquareRootTool:
    def __init__(self):
        self.name = "square_root"
        self.func = self.run
        self.description = "Computes the square root of a non-negative number."
        self.parameters = {
            "a": "The number (int or float) for which to compute the square root."
        }
        self.returns = "float"
    
    def run(self, a: float) -> float:
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
