from fastapi import APIRouter, Body, status, HTTPException
from models.auth_model import UserRegisterModel, UserLoginModel
from models.response_model import UserRegisteredModel, UserRegisterError
from database.database import users
from fastapi.responses import JSONResponse
from core.utils import error_response


router = APIRouter()


@router.post("/register")
def user_register(request: UserRegisterModel = Body(...)):
    try:
        if (user := users.find_one({"$or": [{"user_name" : request.user_name},{"mobile_number" : request.contact}] })) is None:
            users.insert_one(request.model_dump())

            return JSONResponse(
                content = UserRegisteredModel(
                    reference_id=request.reference_id,
                    username=request.user_name,
                    email_id=request.email_id,
                    created_at= str(request.created_at)
                ).model_dump(),
                status_code = status.HTTP_201_CREATED
            )
        
        else:
            return error_response(
                code = "E101", 
                description = "Username or mobile already exists"
            )
        
    except Exception as err:
        return str(err)


@router.post("/login")
async def user_login(request: UserLoginModel):
    try:
        return request.model_dump()
    
    except Exception as err:
        return str(err)
