from typing import Annotated
from fastapi import status, Form, UploadFile, File, HTTPException, APIRouter, Depends
from starlette.status import HTTP_202_ACCEPTED
from .. import model, utils
from sqlalchemy.orm import Session

from .. database import get_db, supabase

router = APIRouter(
    tags=["User"],
    prefix="/users"
    )
 


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
        file_content = await profile_pic.read()
        try:
            response = supabase.storage.from_("Bucket").upload(
                path=file_location,
                file=file_content,
                file_options={"content-type": str(profile_pic.content_type)} 
            )
            if hasattr(response, 'error') and response.error:
                raise HTTPException(status_code=500, detail="Error uploading profile picture")

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error uploading profile picture: {str(e)}")

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
