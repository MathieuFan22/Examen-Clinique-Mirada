import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


class Settings(BaseSettings):
    """Application base setting"""
    ROOT_PATH: str = os.getenv("ROOT_PATH", "")
    PORT: str = os.getenv("PORT", "3000")
    model_config = SettingsConfigDict()

load_dotenv() # This line loads the variables from the .env file
settings = Settings()