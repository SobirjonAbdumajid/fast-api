from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.core.database.config import get_general_session

router = APIRouter()


@router.get("/test")
async def test(
        session: AsyncSession = Depends(get_general_session)
):
    test_sql = text("""SELECT * FROM students""")
    result = await session.execute(test_sql)
    map_res = result.mappings().all()
    return map_res
