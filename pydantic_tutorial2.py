''' Here we learn about 
Field Validator '''
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    name: str 
    age: int 
    weight: float 
    married: Optional[bool] = False
    allergies: Optional[List[str]] = "None"
    email: EmailStr
    contact_details: Dict[str, str]

    @field_validator('email') #Here we want to check if the patient's is tie-up bank employee?
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
    #abc@gmail.com
        domain_name = value.split('@')[-1] #So that our Domain name should contain the part after @

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name') #Here we will make our name in uppercase letters
    @classmethod
    def transform_name(cls, value):
        return value.upper()



def insert_patient_data(P: patient):
    print(P.name)
    print(P.age)
    print("Inserted")

def update_patient_data(Patient: patient):
    print(f"Name is: {Patient.name}")
    print(f"Age is: {Patient.age}")
    print(f"Weight is:{Patient.weight}")
    print(f"Marriage status is (True or False?):{Patient.married}")
    print(f"Any Allergies?: {Patient.allergies}")
    print(f"Contact number is: {Patient.contact_details}")
    print(f"Email is: {Patient.email}")
    print("Updated")

patient_info = {"name": "Satish Singh", 
                  "age": 30, 
                  "weight": 75.5, 
                  "married": True, 
                  "allergies": ["Pollen", "Dust"], 
                  "email": "abc@hdfc.com",
                  "contact_details": {"phone": "8755857000"}
                  }

patient_1 = patient(**patient_info)

insert_patient_data(patient_1)
update_patient_data(patient_1)