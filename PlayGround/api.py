from fastapi import FastAPI #importing the FastAPI Class

app = FastAPI() # Instance of the FastAPI application

@app.get("/") # Route 1 or endpoint 1
def root(): 
    return {"message": "Hello FastAPI"}

@app.get("/items/{item_Id}") # Route 2
def get_item(item_Id: int):
    return {"item_Id": item_Id}
