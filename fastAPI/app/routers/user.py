from typing import Annotated, List
from fastapi import Query, status, Form, UploadFile, File, HTTPException, APIRouter, Depends
from pydantic import EmailStr
from .. import model, utils, schemas
from sqlalchemy.orm import Session
from .. database import get_db

router = APIRouter(
    tags=["User"],
    prefix="/users"
    )

@router.post('/guide', status_code=status.HTTP_201_CREATED, response_model=schemas.guide_out)
async def create_guide(
    name: Annotated[str, Form()], 
    email: Annotated[EmailStr, Form()],
    gender: Annotated[str, Form()],
    country: Annotated[str, Form()],
    phone: Annotated[str, Form(),],
    address: Annotated[str, Form()],
    password: Annotated[str, Form(),],
    confirm_password: Annotated[str, Form(),],
    age: Annotated[int, Form(), ],
    biography: Annotated[str, Form(),],
    languages: Annotated[List[str], Form()],
    specialization: Annotated[str, Form()],
    availability: Annotated[str, Form()],
    additional_skills: Annotated[List[str], Form()],
    payment_methods: Annotated[List[str], Form()], 
    profile_pic: Annotated[UploadFile, File()], 
    otp: Annotated[str, Form(),],
    db:Session = Depends(get_db)): 

    if(password != confirm_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Password not matched")

    #checking existing mail in database
    email_query = db.query(model.Guide).filter(model.Guide.email == email)
    email_found = email_query.first()
    #verify OTP
    if not utils.verify_otp(email, otp):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP")

    if email_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user with email already exist")
    else:
        hashed_password = utils.hash(password)
        password = hashed_password
        file_location = f"user/{email}{profile_pic.filename}"
        await utils.uploadImage(profile_pic, file_location)
        new_guide = model.Guide(
            user_name= name,
            email= email, 
            gender= gender,
            country= country,
            phone= phone,
            address = address,
            password= password,
            age=age,
            biography= biography,
            languages= languages,
            specialization = specialization,
            availability = availability,
            additional_skills = additional_skills,
            payment_methods = payment_methods,
            profile_pic = file_location
        )
    db.add(new_guide)
    db.commit()

    return new_guide 



@router.post('/visitor', status_code=status.HTTP_201_CREATED)
async def create_user( 
    name: Annotated[str, Form()],
    email: Annotated[str, Form()],
    gender:Annotated[str, Form()],
    country: Annotated[str, Form()],
    phone: Annotated[str, Form()],
    password: Annotated[str, Form()],
    confirm_password: Annotated[str, Form()],
    otp: Annotated[str, Form()],
    profile_pic: Annotated[UploadFile, File()],
  db:Session = Depends(get_db)):
    #checking passwords
    if(password != confirm_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Password not matched")

    #checking existing mail in database
    email_query = db.query(model.Visitor).filter(model.Visitor.email == email)
    email_found = email_query.first()
    if email_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user with email already exist")

    #verify OTP
    #if not utils.verify_otp(email, otp):
    #    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP")

    else:
        hashed_password = utils.hash(password)
        password = hashed_password
        file_location = f"user/{email}{profile_pic.filename}"
        await utils.uploadImage(profile_pic, file_location)
        new_user =model.Visitor(user_name = name, email = email, password = password,
                                gender= gender, country= country, phone = phone,
                                profile_pic= file_location)
        db.add(new_user)
        db.commit()
        return {"Message": "Welcome to whatever this"}


@router.post("/verify",status_code=status.HTTP_202_ACCEPTED)
async def verify(email: Annotated[str, Form()]):
    otp = utils.generate_otp()
    utils.save_otp(email, otp)
    await utils.send_mail(email, otp);
    return HTTPException(status_code=202, detail="OTP is sent to the mail")
