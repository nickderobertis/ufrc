from typing import Final

from pydantic import BaseSettings


class Settings(BaseSettings):
    username: str
    password: str
    uid: int
    group_name: str

    class Config:
        env_file = ".env"
        env_prefix = "UFRC_"


SETTINGS: Final[Settings] = Settings()
