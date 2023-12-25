from fastapi import APIRouter
from main import app

app = APIRouter()


env: str = "DEV"

if env == "DEV":
    # Database details
    DATABASE_NAME = "project_start"



elif env == "UAT":
    # Database details
    DATABASE_NAME = "project_start"


elif env == "PROD":
    # Database details
    DATABASE_NAME = "project_start"

