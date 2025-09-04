# Day - 8
# Author - Leo Programmer - 011
# Date - 2025-09-04
# Day 8: FastAPI - Field Validation with Pydantic

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# Field()
'''
Field() comes from Pydantic.

It allows you to add extra metadata & validation rules to your model fields.

More powerful than just using plain str, int, etc.

from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, regex="^[a-zA-Z0-9_]+$")
    age: int = Field(..., ge=18, le=100)  # ge = greater or equal, le = less or equal
    bio: str = Field(default="No bio provided", max_length=150)

Important Parameters:

- default → sets a default value.

- ... (ellipsis) → means required field.

- min_length, max_length → for strings.

- ge, le → for numbers (greater equal, less equal).

- regex → enforce a pattern (like only alphanumeric usernames).

- description → adds documentation for Swagger UI (FastAPI Docs).
'''

class CreateUser(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="Username must be between 3 and 20 characters and no special characters except an underscore.", pattern="^[a-zA-Z0-9_]+$")
    password: str = Field(..., min_length=3, max_length=50,  description="Password must be between 8 and 50 characters.")
    age: int = Field(..., ge=13, le=120, description="Age must be between 13 and 120.")
    bio: str = Field(default="Bio not provided.", max_length=150, description="Bio must not exceed 150 characters.")

@app.post("/create_user")
def create_user(user: CreateUser):
    return {"status": "User Created Successfully!", "user": user}
