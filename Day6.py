# Day - 6 Pydantic Basics (models, type checking, default values).
# Author - Leo Programmer - 011
# Date - 2025-09-02

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

'''
What is Pydantic?

Pydantic is a data validation and parsing library used in FastAPI (and other Python apps).

It ensures that data coming from outside (like API requests) is in the correct format before your backend logic runs.

It’s built on Python type hints (int, str, float, List, etc.) and uses them to validate input data automatically.

In FastAPI, every request body, query parameter, or response schema is powered by Pydantic models.

Why Pydantic in FastAPI?

Automatic data validation (wrong type = error).
Converts input to correct type when possible (e.g., "123" → int).
JSON schema auto-generation (Swagger UI docs).
Helps keep code clean, reliable, and bug-free.
'''

class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True

@app.post("/createpost")
def create_post(new_post: Post):
    return {"message": "Post Created Successfully!", "data": new_post}

'''
Here, post: Post means → FastAPI will expect JSON data in the request body.

FastAPI takes that JSON, and automatically creates a Post object from it.

So post is an object (instance) of the Post class, not the class itself.

FastAPI then returns that error in a structured JSON format with details:

{
    type: what went wrong (bool_parsing)

    loc: where in the request it failed (body → published)

    msg: human-friendly message

    input: the actual bad value you sent
}

This is the special power of Pydantic + FastAPI → you don’t need to write custom error handling for each field. It’s automatic, consistent, and user-friendly.
'''