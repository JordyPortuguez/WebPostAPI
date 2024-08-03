from pydantic import BaseModel
from typing import Optional


class PostBase(BaseModel):
    Id:   Optional[int] = None
    Content: str
    Title: str

    class Config:
        from_attributes = True


class CreatePost(PostBase):
    class Config:
        from_attributes = True