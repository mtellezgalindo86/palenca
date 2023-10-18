from pydantic import BaseModel
from typing import List, Optional


class EmploymentFile(BaseModel):
    url: str
    file_type: str


class EmploymentHistory(BaseModel):
    employer: str
    start_date: str
    end_date: Optional[str]
    federal_entity: str
    base_salary: float
    monthly_salary: float


class EmploymentData(BaseModel):
    account_id: str
    employment_info: dict
    employment_history: List[EmploymentHistory]
    employment_events: Optional[dict]
