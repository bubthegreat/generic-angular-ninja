
from typing import Optional
from ninja import Schema
from datetime import date



class EmployeePost(Schema):
    first_name: str
    last_name: str
    department_id: Optional[int] = None
    birthdate: Optional[date] = None

class EmployeeGet(Schema):
    id: int
    first_name: str
    last_name: str
    department_id: Optional[int] = None
    birthdate: Optional[date] = None

    
class DepartmentPost(Schema):
    title: str

class DepartmentGet(Schema):
    id: int
    title: str
