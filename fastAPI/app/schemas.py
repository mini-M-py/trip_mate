from typing import List
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

class create_plan(BaseModel):
    title: str
    discription: str
    tour_type: str
    transportation: str
    reviews_count: int
    price: int

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
    additional_skills: List[str]
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
    payment_methods: List[str] 

    class Config:
        from_attributes = True



class dummy_user(BaseModel):
    user_name: str
    email: EmailStr
    password: str 
