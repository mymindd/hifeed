from app.models.domain.users import User
from pydantic import BaseModel

class UserWithToken(User):
    token: str


class UserInLogin(BaseModel):
    # email: EmailStr
    password: str


class UserInResponse(BaseModel):
    user: UserWithToken