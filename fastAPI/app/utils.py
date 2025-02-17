from fastapi import UploadFile, status, HTTPException
from passlib.context import CryptContext
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig 
from cachetools import TTLCache
from .config import settings
from .database import supabase
from random import randint

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = 'auto')

otpCache = TTLCache(maxsize=1000, ttl=120)

async def uploadImage(image: UploadFile, file_location: str):
    file_content = await image.read()
    try:
        response = supabase.storage.from_("Bucket").upload(
                path=file_location,
                file=file_content,
                file_options={"content-type": str(image.content_type)} 
            )
        if hasattr(response, 'error') and response.error:
              raise HTTPException(status_code=500, detail="Error uploading profile picture")

    except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error uploading profile picture: {str(e)}")



async def send_mail(email: str, otp: str):
    conf = ConnectionConfig(
        MAIL_USERNAME = settings.mail_username,
        MAIL_PASSWORD = settings.mail_password,
        MAIL_FROM = settings.mail_from,
        MAIL_PORT = 465,
        MAIL_SERVER = "smtp.gmail.com",
        MAIL_STARTTLS = False,
        MAIL_SSL_TLS = True,
        USE_CREDENTIALS = True,
        VALIDATE_CERTS = True
            )
    message = MessageSchema(
            subject="Verify Your Email",
            recipients=[email],
            body=f"""
            <h2>verification email</h2>
            <p>Hi there,</p>
            <p>Your verification code is: <strong>{ otp }</strong></p>
            <p>Please use this code to verify your account or complete the desired action.</p>
            <p>This code is valid for a limited time period.</p>
            <br>
            <p class="footer">Best regards,</p>
            <p class="footer">Your Application</p> 
            """,
            subtype='html'
        )
        
    fm = FastMail(conf)
    await fm.send_message(message)


def hash(password:str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def generate_otp():
    return  str(randint(9999, 100000)) 

def save_otp(email, otp):
    otpCache[email] = otp

def verify_otp(email: str, otp:str) -> bool:
    cached_otp = otpCache.get(email)

    if cached_otp is None:
        raise   HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OTP expired")
    
    if cached_otp != otp:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP")
    
    del otpCache[email]

    return True

