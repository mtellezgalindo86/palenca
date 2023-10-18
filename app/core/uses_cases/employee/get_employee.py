from app.adapters.employee.employee import EmployeeAdapter as GetEmployeeAdapter


class GetEmployee:
    def __init__(self, external_service: GetEmployeeAdapter):
        self.external_service = external_service

    def get_employee(self, account_id):
        response = self.external_service.get_info_employee(account_id)
        return response
