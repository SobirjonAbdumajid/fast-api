from fastapi import Depends
from app.api.repositories.bookings import BookingRepository
from app.api.schemas.bookings import BookingSchema


class BookingController:
    def __init__(self, bookings_repo: BookingRepository = Depends()):
        self.__bookings_repo = bookings_repo

    async def make_booking(self, data: BookingSchema):
        day = (data.check_out - data.check_in).days
        room_price = await self.__bookings_repo.get_room_price(data.room_id)
        total_price = room_price * day
        return await self.__bookings_repo.make_booking(data, total_price)
