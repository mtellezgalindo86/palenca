from pydantic import BaseModel


class Employee(BaseModel):
    identifier: str
    country: str
    platform: str
