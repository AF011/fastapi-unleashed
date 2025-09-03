# Day 7: FastAPI - User Login Endpoint with Pydantic Validation
# Author - Leo Programmer - 011
# Date - 2025-09-03

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

class LoginData(BaseModel):
    username: str
    password: str
    email: EmailStr
    remember_me: Optional[bool] = False

fake_db = {
    "leo011": {"password": "AF011", "email": "leo011@gmail.com"},
    "pheonix-02": {"password": "PX-02", "email": "ph02@gmail.com"}    
}

@app.post("/login")
def Login(data: LoginData):
    
    if data.username in fake_db:
        if data.password == fake_db[data.username]["password"]:
            return {"status": "Login Successful!", "message": f"Welcome back, {data.username}", "remember_me": data.remember_me}
        return {"status": "Login Failed!", "message": "Invalid Password!"}        
    
    return {"status": "Login Failed!", "message": "Invalid Credentials!"}
