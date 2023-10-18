import requests
from app.core.entities.account.account_get_data import AccountResponse


class AccountAdapter:
    @staticmethod
    def get_account(account_id) -> AccountResponse:
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'private_8174d04a_8384_4994_af9f_7881ecff294c'
        }
        response = requests.get(
            f'https://sandbox.palenca.com/v1/accounts/{account_id}',
            headers=headers
        )
        response_data = response.json()
        if response_data is None:
            return ("No se encontraron datos en la respuesta")

        profile_data = AccountResponse(**response_data)
        return profile_data
