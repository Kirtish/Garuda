from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    database_url: str = Field("sqlite:///./garuda.db", env="DATABASE_URL")
    research_dir: str = Field("./research", env="RESEARCH_DIR")
    app_name: str = Field("Garuda", env="APP_NAME")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
