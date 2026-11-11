from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=4000)
    top_k: int = Field(default=5, ge=1, le=15)

class FeedbackRequest(BaseModel):
    question: str
    answer: str
    rating: int = Field(ge=1, le=5)
    comment: str | None = None
