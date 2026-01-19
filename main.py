# python3 -m env env_name
# source env_name/bin/activate
# pip install fastapi uvicorn pydantic
from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
        return data

@app.get("/")
def Welcome():
    return {'message': 'Patient Management System API'}
    

@app.get("/about")
def about():
    return {'message': 'A fully functional API to manage your patients records'}
    

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = "Patient Id in the DataBase", example = "P001")): 
    # ..., -> suggets it's a Required Parameter
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = 'patient not found')

@app.get("/sort")
def sort_patient(sort_by: str = Query(..., description = "Patients can be sort by Height, Weight or BMI"), 
                   order: str = Query('asc' , description = "sort in ascending or descending order")):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, description = f"Choose from {valid_fields}")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code = 400, description = "Choose from asc or desc")
    
    data = load_data()
    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse = sort_order)

    return sorted_data

    



