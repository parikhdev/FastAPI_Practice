''' Introduction: Pydantic is mainly used for Data Validation...
Here we leared about the
1) (typing module) from where we can import List,Dict, 
 Optional[For Optional values also set default value],
 Annotated [We can define the dataType and can provide Field function inside it],
2) (pydantic module) from where we can import Basemodel[Necessary for classes], 
EmailStr[To Check Strings are email or not], 
AnyUrl[To check any Link Url], 
Field[It's very important we can put many restrictions through it like max_length, (ge, gt, lt, le), default, strict for strict DataTypes, Title, Description, Examples]'''

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    name: str = Field(max_length = 50) # Name should not be greater than 50 characters
    age: int = Field(gt = 0, lt=120) # Age should be between (0-120)
    weight: float = Field(gt = 0) # Weight should not be negative
    married: Optional[bool] = False
    allergies: Optional[List[str]] = "None"
    email: EmailStr
    contact_details: Dict[str, str]
    link: Annotated[AnyUrl, Field(default = None, title = 'Facebook Link', description = "Give the User's Facebook Link", example = 'https://facebook.com')] # Combo of Annotated and Field
    salary: Annotated[float, Field(strict = True)] # Now if someone enter salary in string it'll throw error

def insert_patient_data(Patient: patient):
    print(Patient.name)
    print(Patient.age)
    print("Inserted")

def update_patient_data(Patient: patient):
    print(f"Name is: {Patient.name}")
    print(f"Age is: {Patient.age}")
    print(f"Weight is:{Patient.weight}")
    print(f"Marriage status is (True or False?):{Patient.married}")
    print(f"Any Allergies?: {Patient.allergies}")
    print(f"Contact number is: {Patient.contact_details}")
    print(f"Email is: {Patient.email}")
    print(f"Profile is: {Patient.link}")
    print(f"Salary is: {Patient.salary}")
    print("Updated")

patient_info = {"name": "Nitish", "age": 30}
patient_update = {"name": "Satish Singh", 
                  "age": 30, 
                  "weight": 75.5, 
                  "married": True, 
                  "allergies": ["Pollen", "Dust"], 
                  "email": "abc@gmail.com",
                  "contact_details": {"phone": "8755857000"},
                  "link": "https://facebook.com",
                  "salary": 1000000
                  }

patient_1 = patient(**patient_update)

# Note: Here if we put the patient_info incomplete dictionary in patient_1 variable or directly pass as a parameter, we will get an (Validation error)
# patient_1 = patient(**patient_info)

insert_patient_data(patient_1)
update_patient_data(patient_1)

# with open("pydantic_tutorial3.py", 'a') as f:
#     f.write("from pydantic import BaseModel, EmailStr, AnyUrl, Field")
#     f.write("from typing import List, Dict, Optional, Annotated")
