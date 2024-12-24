from fastapi import APIRouter, Depends
from app.api.controller.bookings import BookingController
from app.api.schemas.bookings import BookingSchema

router = APIRouter()


@router.post("/create_booking")
async def make_booking(
    booking: BookingSchema,
    controller: BookingController = Depends()
):
    return await controller.make_booking(booking)
