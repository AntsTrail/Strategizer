from langchain.tools import Tool

class ProductTool(Tool):
    """
    Tool that computes the product of two numbers.
    """

    def __init__(self):
        # Initialize with required arguments
        super().__init__(
            name="product",
            func=self.run,
            description="Computes the product of two numbers."
        )

    def run(self, a: float, b: float) -> float:
        """
        Returns the product of two numbers.

        Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

        Returns:
        int or float: The product of the two numbers.
        """
        return a * b
