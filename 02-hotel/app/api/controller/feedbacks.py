from fastapi import Depends
from app.api.repositories.feedbacks import FeedbackRepository
from app.api.schemas.feedbacks import FeedbackSchema


class FeedbackController:
    def __init__(self, feedback_repo: FeedbackRepository = Depends()):
        self.feedback_repo = feedback_repo

    async def make_feedback(self, data: FeedbackSchema):
        return await self.feedback_repo.make_feedback(data)
