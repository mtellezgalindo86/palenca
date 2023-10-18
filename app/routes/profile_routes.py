from fastapi import APIRouter
from app.adapters.profile.profile import ProfileAdapter
from app.core.uses_cases.profile.get_profile import GetProfile
from app.core.entities.profile.profiler_get_data import ProfileData

router = APIRouter()

external_service_profile = ProfileAdapter()
get_profile_because = GetProfile(external_service_profile)


@router.get("/get_profile/{account_id}", response_model=ProfileData)
def get_profile_handler(account_id: str):
    response = get_profile_because.get_profile(account_id)
    return response
