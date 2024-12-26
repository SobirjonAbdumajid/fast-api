from pydantic import BaseModel


class FeedbackSchema(BaseModel):
    user_id: int
    room_id: int
    comment: str
