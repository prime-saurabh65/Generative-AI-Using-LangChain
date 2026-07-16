from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    # name: str
    name: str = "Saurabh"   # name is by default set to 'Saurabh'
    age: Optional[int] = None   # age is by default set to None
    email: Optional[EmailStr] = None
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representating cgpa of the student')

new_student1 = {'name': 'Saurabh', 'age':35, 'cgpa':8}
new_student2 = {'age':'32', 'email':'abc@gmail.com'}     # Pydantic do implicit type conversion to '32' to 32.


student = Student(**new_student2)

# model_dump() is a Pydantic method that converts a Pydantic model object into a Python dictionary.
student_dict = student.model_dump()
student_json = student.model_dump_json()

print(student_dict['email'])