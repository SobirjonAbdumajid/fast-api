from fastapi import Depends

from app.api.repositories.rooms import RoomsRepository, RoomsDetailsRepository


class RoomsController:
    def __init__(
            self,
            rooms_repo: RoomsRepository = Depends()
    ):
        self.__rooms_repo = rooms_repo

    async def get_rooms(self):
        return await self.__rooms_repo.get_all_rooms()


class RoomsDetailsController:
    def __init__(
            self,
            rooms_details_repo: RoomsDetailsRepository = Depends()
    ):
        self.__rooms_details_repo = rooms_details_repo

    async def get_room_details(self, room_id: int):
        return await self.__rooms_details_repo.get_room_by_id(room_id)

    async def get_room_details_with_feedbacks(self, room_id: int):
        return await self.__rooms_details_repo.get_room_with_feedbacks(room_id)


