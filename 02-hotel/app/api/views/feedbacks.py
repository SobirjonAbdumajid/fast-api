from fastapi import Depends, FastAPI, status, APIRouter
from app.api.schemas.feedbacks import FeedbackSchema
from app.api.controller.feedbacks import FeedbackRepository

router = APIRouter()

@router.post("/")
async def make_feedback(feedback: FeedbackSchema, controller: FeedbackRepository = Depends()):
    return await controller.make_feedback(feedback)

