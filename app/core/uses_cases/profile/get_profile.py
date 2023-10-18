from app.adapters.profile.profile import ProfileAdapter as ProfileAdapter


class GetProfile:
    def __init__(self, external_service: ProfileAdapter):
        self.external_service = external_service

    def get_profile(self, account_id):
        response = self.external_service.get_account_profile(account_id)
        return response
