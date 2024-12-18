from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.models.base import Base


class Rooms(Base):
    __tablename__ = 'rooms'

    room_number: Mapped[int]
    room_type: Mapped[str] = mapped_column(ForeignKey('room_types.id'))
    price: Mapped[float]
    status: Mapped[str] = mapped_column(ForeignKey('room_statuses.id'))


class RoomsType(Base):
    __tablename__ = 'room_types'

    title: Mapped[str]


class RoomsStatus(Base):
    __tablename__ = 'room_statuses'

    title: Mapped[str]