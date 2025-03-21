from langchain.tools import Tool

class QuotientTool(Tool):
    """
    Tool that computes the quotient of two numbers (a divided by b).
    """

    def __init__(self):
        # Initialize with required arguments
        super().__init__(
            name="quotient",
            func=self.run,
            description="Computes the quotient of two numbers (dividing the numerator by the denominator)."
        )

    def run(self, a: float, b: float) -> float:
        """
        Returns the quotient of two numbers (a divided by b).

        Parameters:
        a (int or float): The numerator.
        b (int or float): The denominator.

        Returns:
        float: The quotient of a and b, or raises a ValueError if b is zero.
        """
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")
