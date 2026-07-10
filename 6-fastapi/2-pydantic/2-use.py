from pydantic import BaseModel,Field,EmailStr,AnyUrl
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="name of the patient",description="Give the name of the patient less than 50 chars",examples=['amit','nitish'])]
    email:EmailStr
    linkedin_url:AnyUrl
    age:int
    weight:Annotated[float, Field(gt=0, strict=True)]
    married:Annotated[bool,Field(default=False,title="Married Status",description="Enter the patient married status in boolean")]
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details: Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")

def updated_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info={"name":"mourya","email":"example@gmail.com","linkedin":"https://linkedin.com","age":"20","weight":75,'married':False,'allergies':['pollen','dust'],'contact_details':{"phone":"1234567890"}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)