from langchain.tools import Tool

class PowerTool(Tool):
    """
    Tool that computes the result of raising the base number to the power of the exponent.
    """

    def __init__(self):
        # Initialize with required arguments
        super().__init__(
            name="power",
            func=self.run,
            description="Computes the result of raising a base number to the power of the exponent."
        )

    def run(self, a: float, b: float) -> float:
        """
        Returns the result of raising the base to the power of the exponent.

        Parameters:
        a (int or float): The base number.
        b (int or float): The exponent.

        Returns:
        int or float: The result of base raised to the power of exponent.
        """
        return a ** b
