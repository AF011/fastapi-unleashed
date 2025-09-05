# Day - 9: Nested Models
# Author - Leo Programmer - 011
# Date - 2025-09-05

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

app = FastAPI()

class Post(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, description="Title must be between 3 and 100 characters.")
    content: str = Field(..., min_length=10, description="Content must be at least 10 characters long.")
    published: Optional[bool] = False

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="Username must be between 3 and 20 characters and no special characters except an underscore.", pattern="^[a-zA-Z0-9_]+$")
    email: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    posts: List[Post] = []
    settings: Dict[str, str] = {"theme": "light", "notifications": "enabled"}
    class Config:
        extra = "forbid"

'''
class Config:
    extra = "ignore"   # default → ignore extra fields silently
    extra = "allow"    # accept extra fields and keep them in the model
    extra = "forbid"   # raise error if extra fields are present
'''

@app.post("/create-user")
def create_user(user: User):
    return {"status": "User Created Successfully!", "user": user}
