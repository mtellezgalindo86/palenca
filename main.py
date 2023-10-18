from fastapi import FastAPI
from app.routes import employee_routes, profile_routes, account_routes

app = FastAPI()

app.include_router(employee_routes.router)
app.include_router(profile_routes.router)
app.include_router(account_routes.router)
