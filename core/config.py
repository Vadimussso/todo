from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: SecretStr

    db_min_pool_size: int
    db_max_pool_size: int

    debug: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
