from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Resume Ranker"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/v1"
    
    class Config:
        case_sensitive = True

settings = Settings() 