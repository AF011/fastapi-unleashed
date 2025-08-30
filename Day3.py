# Day3 - GET VS POST Requests
# Author: The Leo Programmer - 011
# Date: 2025-08-30

from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/get-data")
def get_item(item_name: str, item_cost: float):
    return {"Item Name": item_name, "Item Cost": item_cost}

@app.post("/add-item")
def add_item(item_name: str = Body(...), item_cost: float = Body(...)):
    return {"message":"Successfully Added the Item", "Item Name": item_name, "Item Cost": item_cost}


# Test using Postman:
# 1. GET Request Example: http://127.0.0.1:8000/get-data?item_name=Apple&item_cost=100
# 2. POST Request Example (Body -> raw JSON):
#    {
#        "item_name": "Apple",
#        "item_cost": 100
#    }
