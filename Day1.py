# Day - 1 : FastAPI Basic Setup 
# Author : Leo Programmer-011
# Date : 2025-08-28

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello Everyone": "Welcome to the Leo Programmer-011 world..!"}