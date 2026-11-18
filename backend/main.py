from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Employee Management API",
    description="Employee Management System",
    version="1.0"
)

class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float
    email: Optional[str] = None

employees = [
    {
        "id": 1,
        "name": "Ravi",
        "department": "Python",
        "salary": 35000,
        "email": "ravi@gmail.com"
    },
    {
        "id": 2,
        "name": "Priya",
        "department": "Data Science",
        "salary": 45000,
        "email": "priya@gmail.com"
    },
    {
        "id": 3,
        "name": "Kiran",
        "department": "SQL",
        "salary": 30000,
        "email": "kiran@gmail.com"
    }
]

@app.get("/")
def home():
    return {"message": "Welcome to Employee Management API"}

@app.get("/employees")
def get_employees():
    return employees

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees", status_code=201)
def create_employee(employee: Employee):
    for emp in employees:
        if emp["id"] == employee.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    employees.append(employee.model_dump())
    return {"message": "Employee created successfully", "employee": employee}

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):
    if employee_id != updated_employee.id:
        raise HTTPException(status_code=400, detail="ID mismatch")

    for index, employee in enumerate(employees):
        if employee["id"] == employee_id:
            employees[index] = updated_employee.model_dump()
            return {"message": "Employee updated successfully"}

    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for index, employee in enumerate(employees):
        if employee["id"] == employee_id:
            deleted = employees.pop(index)
            return {"message": "Employee deleted successfully", "employee": deleted}

    raise HTTPException(status_code=404, detail="Employee not found")