from fastapi import APIRouter
from app.adapters.account.account import AccountAdapter
from app.core.uses_cases.account.get_account import GetAccount
from app.core.entities.account.account_get_data import AccountResponse

router = APIRouter()

external_service_account = AccountAdapter()
get_account_because = GetAccount(external_service_account)


@router.get("/get_account/{account_id}", response_model=AccountResponse)
def get_account_handler(account_id: str):
    response = get_account_because.get_account(account_id)
    return response
