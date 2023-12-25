from pydantic import (BaseModel, Field, UUID4)
from datetime import datetime
import uuid

class UserRegisterModel(BaseModel):
    reference_id: str | None = str(uuid.uuid4())
    user_name: str = Field(...)
    name:  str = Field(...)
    contact:  str = Field(...)
    email_id:  str = Field(...)
    password:  str = Field(...)
    address:  str | None = None
    city:  str | None = None
    state:  str | None = None
    country:  str | None = None
    created_at : datetime | None = datetime.now()
    is_active: bool = True

class UserLoginModel(BaseModel):
    user_name: str = Field(...)
    password: str = Field(...)

class Users(BaseModel): 
    reference_id : str   
    user_name: str
    first_name: str
    last_name: str
    email_id: str
    password: str
    mobile_number: str
    address: str
    city: str
    state: str
    country: str
    is_active: bool





    