from typing import Optional

from pydantic import BaseConfig, BaseModel


class User(BaseModel):
    username: str
    email: str
    bio: str = ""
    image: Optional[str] = None
