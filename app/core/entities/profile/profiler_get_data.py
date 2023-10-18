from pydantic import BaseModel
from typing import Optional, List


class Profile(BaseModel):
    first_name: str
    last_name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    city_name: Optional[str] = None
    birthday: str
    picture_url: Optional[str] = None


class IdInfo(BaseModel):
    type: str
    name: str
    value: str


class Data(BaseModel):
    account_id: str
    profile: Profile
    bank_info: Optional[dict] = None
    vehicle_info: Optional[dict] = None
    metrics_info: Optional[dict] = None
    ids_info: List[IdInfo]


class ProfileData(BaseModel):
    data: Data
