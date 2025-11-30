from pydantic_settings import BaseSettings

## Configuration for the application settings
class Settings(BaseSettings):
    PROJECT_NAME: str = "Project Omission"
    API_V1_STR: str = "/api/v1"
    API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()