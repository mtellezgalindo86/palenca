import requests
from app.core.entities.profile.profiler_get_data import ProfileData


class ProfileAdapter:
    @staticmethod
    def get_account_profile(account_id) -> ProfileData:
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'private_8174d04a_8384_4994_af9f_7881ecff294c'
        }
        response = requests.get(
            f'https://sandbox.palenca.com/v1/accounts/{account_id}/profile',
            headers=headers
        )
        response_data = response.json()
        if response_data is None:
            return ("No se encontraron datos en la respuesta")

        profile_data = ProfileData(**response_data)
        return profile_data
