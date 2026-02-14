from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class createUser(BaseModel):
    name: Annotated[str, Field(max_length = 50, title = "name of the user" )]
    age: int = Field(gt = 0, le = 120)

@app.post("/users")
def create_User(user: createUser):
    return {
        "message": "User created successfully",
        "data": user
    }

@app.get("/hello/{name}")
def get_name(name:str):
    return {"Message": f"Hello {name}"}

@app.get("/square/{number}")
def get_square(number:int):
    return {"Square": number * number}

@app.get("/search")
def search(q:str, limit:int=100):
    return {
        "query": q,
        "limit": limit
        }

@app.get("/users/{user_id}/posts")
def get_userid(user_id:int,page:int=1,size:int=10):
    return {
        "User_id": user_id,
        "Page": page,
        "size": size
        }

@app.get("/products")
def get_product(
    category:str | None = None, 
    min_price:int | None = None,
    max_price:int | None = None
    ):
    return{
        "Category": category,
        "Minimum Price": min_price,
        "Maximum Price": max_price
        }

@app.get("/orders/{order_id}")
def get_order(order_id:int,status:str="check_status"):
    return{
        "Order id": order_id,
        "Status is": status
        }

@app.get("/users/{user_id}/bmi")
def user_details(user_id:int,user_bmi:int=0):
    return{
        "user Id": user_id,
        "user_bmi": user_bmi
        }

@app.get("/customer/{customer_id}/orders")
def get_orders(customer_id: int, status:str | None = None):
    return {
        "customer_id": customer_id,
        "order_status": status
    }