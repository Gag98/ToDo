"""Initialization of the application settings using environment variables."""

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Loading environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    """Class for application settings configuration.

    Attributes
    ----------
    app_name : str
        The name of the application, loaded from the environment variable NAME_APP.
    db_url : str
        The database URL for SQLAlchemy, loaded from the environment variable SQLALCHEMY_DATABASE_URI.
    """

    app_name: str = os.getenv("NAME_APP")
    db_url: str = os.getenv("SQLALCHEMY_DATABASE_URI")

    class Config:
        """Configuration class for setting up the environment file location."""

        env_file: str = "../.env"


# Create an instance of the application settings
settings = Settings()