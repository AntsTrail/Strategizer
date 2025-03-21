from langchain.tools import Tool

class ModuloTool(Tool):
    """
    Tool that returns the remainder when one number is divided by another.
    """

    def __init__(self):
        # Initialize with required arguments
        super().__init__(
            name="modulo",
            func=self.run,
            description="Returns the remainder when one number is divided by another."
        )

    def run(self, a: float, b: float) -> float:
        """
        Returns the remainder when a is divided by b.

        Parameters:
        a (int or float): The dividend.
        b (int or float): The divisor.

        Returns:
        int or float: The remainder of the division.
        """
        return a % b
