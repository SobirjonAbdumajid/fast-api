from fastapi import APIRouter, Depends
from starlette import status
from app.api.schemas.auth import UserInSchema
from fastapi.security import OAuth2PasswordRequestForm
from app.api.controller.auth import AuthController

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: UserInSchema,
    controller: AuthController = Depends()
):
    return await controller.create_user(data=data)


@router.post(
    "/token",
    status_code=status.HTTP_200_OK,
)
async def get_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        controller: AuthController = Depends()
):
    return await controller.check_user(data=form_data)
