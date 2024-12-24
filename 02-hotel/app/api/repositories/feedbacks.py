from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.config import get_general_session
from app.api.schemas.feedbacks import FeedbackSchema
from app.api.models.feedback import FeedBack


class FeedbackRepository:
    def __init__(self, session: AsyncSession = Depends(get_general_session)):
        self.session = session

    async def make_feedback(self, data: FeedbackSchema):
        feedback = FeedBack(**data.dict())
        self.session.add(feedback)
        await self.session.commit()
        await self.session.refresh(feedback)
        return feedback
