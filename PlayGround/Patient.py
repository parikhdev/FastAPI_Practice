from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'
        
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female', 'others']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


def load_data():
    with open('newPatients.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('newPatients.json', 'w') as f:
        json.dump(data, f)


@app.get("/view/{patient_id}")
def showPatientId(patient_id: str = Path(..., description = "The id of the patient", examples = ["P001"])):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code = 404, detail = "Patient not found")

@app.get("/view")
def showData():
    data = load_data()
    return data

@app.post("/create")
def createPatient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code = 400, detail = "Patient already in the data")
    data[patient.id] = patient.model_dump(exclude = ['id'])
    save_data(data)
    return JSONResponse(status_code = 201, content = {"message": "Patient added successfully"})

@app.put("/edit/{patient_id}")
def UpdatePatient(patient_id: str, patient: PatientUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code = 404, detail = "Patient not found")
    existing_Patient_details = data[patient_id]
    updated_Patient_details = patient.model_dump(exclude_unset = True)

    for key, value in updated_Patient_details.items():
        existing_Patient_details[key] = value

    existing_Patient_details['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_Patient_details)
    existing_Patient_details = patient_pydantic_obj.model_dump(exclude = ['id'])

    data[patient_id] = existing_Patient_details
    save_data(data)

    return JSONResponse(status_code = 200, content= {"message": "Patient Updated Successfully"})

