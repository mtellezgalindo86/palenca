from app.core.entities.employee.employee_create import Employee
from app.adapters.employee.employee import EmployeeAdapter as EmployeeCreate


class CreateEmployee:
    def __init__(self, external_service: EmployeeCreate):
        self.external_service = external_service

    def execute(self, data: Employee) -> dict:
        employee = Employee(**data.dict())
        response = self.external_service.create_employee(employee)
        return response
