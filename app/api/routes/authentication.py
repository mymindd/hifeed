from fastapi import APIRouter, Body, Depends, HTTPException, status
from app.models.schemas.users import (
    UserInResponse,
    UserWithToken,
    UserInLogin,
)
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/login", response_model=UserInResponse, name="auth:login")
async def login(
    user_login: UserInLogin = Body(..., embed=True, alias="user"),
) -> UserInResponse:
    # print(user_login.password)
    return UserInResponse(user=UserWithToken(
            username="username",
            email="user.email",
            bio="user.bio",
            image="user.image",
            token="token",
        ),)