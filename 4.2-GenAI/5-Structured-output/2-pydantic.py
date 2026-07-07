from pydantic import BaseModel,EmailStr,Field #understands on it's on even str can convert int
from typing import Optional


class Student(BaseModel):
    name:str = "xyz " #can set default values
    age: Optional[int]=None
    email:EmailStr
    cgpa: float =Field(gt=0,lt=10,default=8.05,description="Decimal value only ") #can set boundaries


new_student={'name':'mourya','email':'abc@ex.com'}

student=Student(**new_student)

student_dict=dict(student)

print(type(student))
#student.name