import os
from dataclasses import dataclass

from dotenv import load_dotenv

# Load environment variables from the .env file.
# The 'override=True' parameter ensures that any existing environment variable values
# are replaced by those in the .env file.
load_dotenv(override=True)


def get_env_value(name: str) -> str:
    """
    Retrieves the environment variable with the specified name.

    This function checks if the environment variable exists in os.environ. If the variable
    is not found, it raises a KeyError with an informative message. This ensures that all
    required environment variables are provided, typically via a .env file.

    Args:
        name (str): The name of the environment variable to retrieve.

    Returns:
        str: The value of the environment variable.

    Raises:
        KeyError: If the environment variable is not present in os.environ.

    Example:
        >>> api_key = get_env_value("OPENAI_API_KEY")
    """
    if name not in os.environ:
        raise KeyError(
            f"Environment variable {name} was not found. Please ensure it is present in your .env file."
        )
    return os.environ[name]


@dataclass
class Config:
    """
    Configuration class for storing environment-based settings.

    This class uses the dataclass decorator to automatically generate initialization and
    representation methods. It retrieves required configuration parameters from the
    environment variables, which are expected to be set in a .env file. For example, the
    OPENAI_API_KEY is loaded from the environment using the get_env_value function.

    Attributes:
        OPENAI_API_KEY (str): API key for accessing OpenAI services.

    Usage:
        >>> config = Config()
        >>> print(config.OPENAI_API_KEY)
    """

    # LLM KEYS
    OPENAI_API_KEY: str = get_env_value("OPENAI_API_KEY")
