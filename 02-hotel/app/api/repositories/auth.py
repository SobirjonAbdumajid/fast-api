from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy import text

from app.core.database.config import get_general_session


class AuthRepository:
    def __init__(self, session: AsyncSession = Depends(get_general_session)) -> None:
        self.session = session
    async def create_user(self, data: dict) -> dict:
        stmt = text(
            """INSERT INTO users (username, first_name, last_name, email, password, is_staff, is_active, is_superuser) VALUES
                    (:username, :first_name, :last_name, :email, :password, :is_staff, :is_active, :is_superuser)"""
        ).bindparams(**data)

        await self.session.execute(stmt)
        await self.session.commit()
        # return {"data": data}

