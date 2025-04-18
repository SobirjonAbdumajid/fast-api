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
                SELECT m.room_number, s.title as room_type, m.price, f.title as status
                FROM rooms as m
                JOIN rooms_status as f ON m.status = f.id
                JOIN rooms_type as s ON m.room_type = s.id where m.id = :room_id;
                """)
        raw_sql2 = text(
            """SELECT users.first_name, feedback.comment FROM feedback JOIN users ON feedback.user_id = users.id JOIN rooms ON rooms.id = feedback.room_id WHERE rooms.id = :room_id;"""
        )
        stmt = await self.session.execute(raw_sql, {"room_id": room_id})
        room = stmt.mappings().first()
        stmt2 = await self.session.execute(raw_sql2, {"room_id": room_id})
        feedback = stmt2.mappings().fetchall()
        feedback_list = [{"first_name": item["first_name"], "comment": item["comment"]} for item in feedback]
        room_data = {
            "room_number": room["room_number"],
            "room_type": room["room_type"],
            "status": room["status"],
            "price": room["price"],
            "feedback": feedback_list,
        }
        return room_data


    # async def get_room_with_feedbacks(self, room_id: int):
    #     raw_sql = text("""
    #     SELECT
    #         r.room_number,
    #         rt.title AS room_type,
    #         r.price,
    #         rs.title AS status,
    #         f.comment AS feedback_comment,
    #         u.username AS feedback_user,
    #         u.first_name AS user_first_name,
    #         u.last_name AS user_last_name
    #     FROM rooms AS r
    #     JOIN rooms_status AS rs ON r.status = rs.id
    #     JOIN rooms_type AS rt ON r.room_type = rt.id
    #     LEFT JOIN feedback AS f ON r.id = f.room_id
    #     LEFT JOIN users AS u ON f.user_id = u.id
    #     WHERE r.id = :room_id
    #     """)
    #     stmt = await self.session.execute(raw_sql, {"room_id": room_id})
    #     return stmt.mappings().all()

    # async def get_room_with_feedbacks(self, room_id: int):
    #     raw_sql = text("""
    #     SELECT
    #         r.room_number,
    #         rt.title AS room_type,
    #         r.price,
    #         rs.title AS status,
    #         f.comment AS feedback_comment,
    #         u.username AS feedback_user,
    #         u.first_name AS user_first_name,
    #         u.last_name AS user_last_name
    #     FROM rooms AS r
    #     JOIN rooms_status AS rs ON r.status = rs.id
    #     JOIN rooms_type AS rt ON r.room_type = rt.id
    #     LEFT JOIN feedback AS f ON r.id = f.room_id
    #     LEFT JOIN users AS u ON f.user_id = u.id
    #     WHERE r.id = :room_id
    #     """)
    #     stmt = await self.session.execute(raw_sql, {"room_id": room_id})
    #     result = stmt.mappings().all()
    #
    #     if result:
    #         room_details = {
    #             "room_number": result[0]["room_number"],
    #             "room_type": result[0]["room_type"],
    #             "price": result[0]["price"],
    #             "status": result[0]["status"],
    #             "feedbacks": [
    #                 {
    #                     "comment": row["feedback_comment"],
    #                     "user": {
    #                         # "username": row["feedback_user"],
    #                         "first_name": row["user_first_name"],
    #                         # "last_name": row["user_last_name"]
    #                     }
    #                 }
    #                 for row in result if row["feedback_comment"] is not None
    #             ]
    #         }
    #         return room_details
    #     return None
    #
