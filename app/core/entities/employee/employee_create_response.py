from pydantic import BaseModel
from typing import List, Optional


class Data(BaseModel):
    user_id: str
    country: str
    platform: str
    account_id: str
    next_step: Optional[str] = None
    methods: List[str] = []
    hint: Optional[str] = None


class CreateEmployeeResponse(BaseModel):
    success: bool
    error: Optional[str] = None
    data: Data
