from app.adapters.account.account import AccountAdapter as AccountAdapter


class GetAccount:
    def __init__(self, external_service: AccountAdapter):
        self.external_service = external_service

    def get_account(self, account_id):
        response = self.external_service.get_account(account_id)
        return response
