from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.config import get_general_session
from app.api.schemas.rooms import RoomsSchema


class RoomsRepository:
    def __init__(
            self,
            session: AsyncSession = Depends(get_general_session),
    ):
        self.session = session

    async def get_all_rooms(self):
        raw_sql = text("""
        SELECT m.room_number, s.title as room_type, m.price, f.title as status
        FROM rooms as m
        JOIN rooms_status as f ON m.status = f.id
        JOIN rooms_type as s ON m.room_type = s.id
        """)
        stmt = await self.session.execute(raw_sql)
        return [RoomsSchema.model_validate(map_res) for map_res in stmt.mappings().all()]


class RoomsDetailsRepository:
    def __init__(
            self,
            session: AsyncSession = Depends(get_general_session),
    ):
        self.session = session

    async def get_room_by_id(self, room_id: int):
        raw_sql = text("""
        SELECT 
            m.room_number, 
            s.title AS room_type, 
            m.price, 
            f.title AS status
        FROM rooms AS m
        JOIN rooms_status AS f ON m.status = f.id
        JOIN rooms_type AS s ON m.room_type = s.id
        WHERE m.id = :room_id
        """)
        stmt = await self.session.execute(raw_sql, {"room_id": room_id})
        result = stmt.mappings().first()

        if result:
            return RoomsSchema.model_validate(result)
        return None

    async def get_room_with_feedbacks(self, room_id: int):
        raw_sql = text("""
        SELECT 
            r.room_number, 
            rt.title AS room_type, 
            r.price, 
            rs.title AS status, 
            f.comment AS feedback_comment, 
            u.username AS feedback_user,
            u.first_name AS user_first_name,
            u.last_name AS user_last_name
        FROM rooms AS r
        JOIN rooms_status AS rs ON r.status = rs.id
        JOIN rooms_type AS rt ON r.room_type = rt.id
        LEFT JOIN feedback AS f ON r.id = f.room_id
        LEFT JOIN users AS u ON f.user_id = u.id
        WHERE r.id = :room_id
        """)
        stmt = await self.session.execute(raw_sql, {"room_id": room_id})
        return stmt.mappings().all()

