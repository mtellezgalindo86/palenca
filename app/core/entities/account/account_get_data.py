from pydantic import BaseModel
from typing import Optional


class AccountInfo(BaseModel):
    account_id: str
    country: str
    platform: str
    identifier: str
    worker_id: str
    last_successful_connection: str
    warning: Optional[str] = None
    status: str
    status_details: Optional[str] = None
    message: Optional[str] = None
    recommendation: Optional[str] = None
    next_step: Optional[str] = None
    created_at: str


class AccountResponse(BaseModel):
    success: bool
    error: Optional[str] = None
    data: AccountInfo
