from pydantic import BaseModel, EmailStr
from fastapi import UploadFile
class create_visitior(BaseModel):
    name: str
    email: EmailStr
    gender: str
    country: str
    phone: str
    password: str
    confirm_password: str
    profile_pic: UploadFile


class dummy_user(BaseModel):
    user_name: str
    email: EmailStr
    password: str 
