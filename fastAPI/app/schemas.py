from typing import List
from pydantic import BaseModel, EmailStr
from fastapi import UploadFile
from sqlalchemy import true
class create_visitior(BaseModel):
    name: str
    email: EmailStr
    gender: str
    country: str
    phone: str
    password: str
    confirm_password: str
    profile_pic: UploadFile

class create_guide(BaseModel):
    name: str
    email: EmailStr
    gender: str
    country: str
    phone: str
    password: str
    confirm_password: str
    age: int
    biography: str
    languages: List[str]
    specialization: str
    availability: str
    group_size: int
    additional_skills: List[str]
    tour_type: str
    transportation: str
    area_covered: List[str]
    payment_method: List[str] 

class guide_out(BaseModel):
    user_name: str
    email: EmailStr
    gender: str
    country: str
    phone: str
    age: int
    biography: str
    languages: List[str]
    specialization: str
    availability: str
    group_size: int
    additional_skills: List[str]
    tour_types: str
    transportation: str
    area_covered: List[str]
    payment_methods: List[str] 

    class Config:
        from_attributes = True



class dummy_user(BaseModel):
    user_name: str
    email: EmailStr
    password: str 
