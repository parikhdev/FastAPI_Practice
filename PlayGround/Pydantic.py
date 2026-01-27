# from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator
from typing import Optional, Annotated
# app = FastAPI()
class user_profile(BaseModel):
    username: Annotated[str, Field(max_length = 50, title = "Name of the user", description = "This field is required")]
    email: Annotated[EmailStr, Field(default = None)]
    age: int = Field(gt = 0, lt = 120)
    website: Annotated[AnyUrl, Field(max_length = 200)]

    @field_validator('email')
    @classmethod
    def email_check(cls, value):
        domain_value = ['hdfc.com', 'icici.com']
        domain_name = value.lower().split('@')[-1]
        if domain_name not in domain_value:
            raise ValueError("Not a valid domain")
        return value


def provide(user: user_profile):
    print(user.username)
    print(user.email)
    print(user.age)
    print(user.website)

Data = {"username": 'Yash', "email": "abc@hdfc.com", "age": 21, "website": "https://www.google.com"}

user1 = user_profile(**Data)

provide(user1)