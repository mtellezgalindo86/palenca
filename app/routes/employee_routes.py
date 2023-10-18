from fastapi import APIRouter, Depends
from app.adapters.employee.employee import EmployeeAdapter
from app.core.uses_cases.employee.create_employee import CreateEmployee
from app.core.uses_cases.employee.get_employee import GetEmployee
from app.core.entities.employee.employee_create_response import CreateEmployeeResponse
from app.core.entities.employee.employee_create import Employee
from app.core.entities.employee.employee_get_data import EmploymentData

router = APIRouter()

external_service = EmployeeAdapter()
create_employee_because = CreateEmployee(external_service)
get_employee_because = GetEmployee(external_service)


@router.post("/create_employee", response_model=CreateEmployeeResponse)
def create_employee_handler(data: Employee):
    response = create_employee_because.execute(data)
    return response


@router.get("/get_employee/{account_id}", response_model=EmploymentData)
def get_employee_handler(account_id: str):
    response = get_employee_because.get_employee(account_id)
    return response
