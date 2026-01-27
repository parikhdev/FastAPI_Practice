from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
def get_name(name:str):
    return {"Message": f"Hello {name}"}

@app.get("/square/{number}")
def get_square(number:int):
    return {"Square of Number": number * number}

@app.get("/search")
def search(q:str, limit:int=100):
    return {"query is": q,
            "limit is": limit}

@app.get("/users/{user_id}/posts")
def get_userid(user_id:int,page:int=1,size:int=10):
    return {"User_id is ": user_id,
            "Page is": page,
            "size is": size}

@app.get("/products")
def get_product(category:str='book',min_price:int=100,max_price:int=1000):
    return{"Category": category,
           "Minimum Price": min_price,
           "Maximum Price": max_price}

@app.get("/orders/{order_id}")
def get_order(order_id:int,status:str="check_status"):
    return{"Order id": order_id,
           "Status is": status}

@app.get("/fastUser/{user_id}")
def user_details(user_id:int,user_bmi:int=0):
    return{"user Id": user_id,
           "user_bmi": user_bmi}
