from fastapi import APIRouter, Depends, HTTPException

from app.api.controller.rooms import RoomsController, RoomsDetailsController

router = APIRouter()


@router.get("")
async def get_rooms(
        controller: RoomsController = Depends()
):
    return await controller.get_rooms()


@router.get("/details/{room_id}", tags=["Rooms"])
async def get_room_details(
        room_id: int,
        controller: RoomsDetailsController = Depends()
):
    room = await controller.get_room_details(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room
