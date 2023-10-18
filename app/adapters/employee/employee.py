import requests
from app.core.entities.employee.employee_create import Employee
from app.core.entities.employee.employee_get_data import EmploymentData


class EmployeeAdapter:

    @staticmethod
    def create_employee(employee: Employee) -> dict:
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'private_8174d04a_8384_4994_af9f_7881ecff294c'
        }

        data = {
            'identifier': employee.identifier,
            'country': employee.country,
            'platform': employee.platform
        }

        response = requests.post('https://sandbox.palenca.com/v1/users/accounts', headers=headers, json=data)
        return response.json()

    @staticmethod
    def get_info_employee(account_id) -> EmploymentData:
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'private_8174d04a_8384_4994_af9f_7881ecff294c'
        }
        response = requests.get(
            f'https://sandbox.palenca.com/v1/accounts/{account_id}/employment',
            headers=headers
        )
        response_data = response.json()['data']
        if response_data is None:
            return ("No se encontraron datos en la respuesta")

        employment_data = EmploymentData(**response_data)

        return employment_data