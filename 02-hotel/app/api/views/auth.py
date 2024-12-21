from fastapi import APIRouter, Depends
from starlette import status
from app.api.schemas.auth import UserInSchema

import schemas
from app.api.controller.auth import AuthController

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: UserInSchema,
    controller: AuthController = Depends()
):
    return await controller.create_user(data=data)
