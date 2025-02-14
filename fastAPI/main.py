from fastapi import FastAPI, HTTPException, Depends, Form, UploadFile, File
from pydantic import BaseModel, EmailStr, constr
from passlib.context import CryptContext
from supabase import create_client, Client
import jwt
import random
import os
from dotenv import load_dotenv
import secrets
from random import randint
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your Next.js frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

secret_key = secrets.token_hex(32) 

load_dotenv()

# Initialize Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")  
SUPABASE_KEY = os.getenv("SUPABASE_KEY")  
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Store OTPs temporarily
otp_store = {}

# JWT Secret Key
SECRET_KEY=secret_key

# Email configuration
conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD'),
    MAIL_FROM = os.getenv('MAIL_FROM'),
    MAIL_PORT = 465,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

# User model
class UserSignup(BaseModel):
    name: str
    email: EmailStr
    gender: str
    country: str
    phone: str
    password: str
    confirm_password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class OTPVerification(BaseModel):
    otp: int

# Signup Route

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/signup")
async def signup(
    name: str = Form(...),
    email: EmailStr = Form(...),
    gender: str = Form(...),
    country: str = Form(...),
    phone: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    profile_pic: UploadFile = File(...)
):
    # Create a user object for validation
    user = UserSignup(
        name=name,
        email=email,
        gender=gender,
        country=country,
        phone=phone,
        password=password,
        confirm_password=confirm_password
    )

    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    # Check if email already exists
    existing_user = supabase.table("users").select("*").eq("email", user.email).execute()
    if existing_user.data:
        raise HTTPException(status_code=400, detail="User already exists")

    # Hash the password
    hashed_password = pwd_context.hash(user.password)

    # Read the file content
    file_content = await profile_pic.read()
    
    # Upload profile picture to Supabase Storage
    file_location = f"users/{email}/{profile_pic.filename}"
    try:
        response = supabase.storage.from_("avatars").upload(
            path=file_location,
            file=file_content,
            file_options={"content-type": profile_pic.content_type}
        )
        if hasattr(response, 'error') and response.error:
            raise HTTPException(status_code=500, detail="Error uploading profile picture")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading profile picture: {str(e)}")

    # Generate 6-digit OTP
    otp = str(randint(100000, 999999))
    
    # Store user data with OTP in database
    user_data = {
        "name": name,
        "email": email,
        "gender": gender,
        "country": country,
        "phone": phone,
        "password": hashed_password,
        "profile_pic": file_location,
        "otp": otp,
        "is_verified": False
    }
    
    try:
        response = supabase.table("users").insert(user_data).execute()
        
        # Send OTP email
        message = MessageSchema(
            subject="Verify Your Email",
            recipients=[email],
            body=f"""
            Hi {name},
            
            Your verification code is: {otp}
            
            This code will expire in 10 minutes.
            """,
            subtype="html"
        )
        
        fm = FastMail(conf)
        await fm.send_message(message)
        
        return {"message": "Signup successful! Please check your email for verification code."}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# OTP Verification Route
@app.post("/verify-otp")
async def verify_otp(verification: OTPVerification):
    try:
        # Convert OTP to string for comparison
        otp_str = str(verification.otp)
        
        # Get user with matching OTP
        response = supabase.table("users").select("*").eq("otp", otp_str).execute()
        
        # Debug logging
        print("OTP:", otp_str)
        print("Response:", response.data)
        
        if not response.data:
            raise HTTPException(status_code=400, detail="Invalid OTP")
        
        user = response.data[0]
        
        # Check if OTP is expired (optional)
        # if is_otp_expired(user['created_at']):
        #     raise HTTPException(status_code=400, detail="OTP has expired")
            
        # Update user as verified
        supabase.table("users").update({
            "is_verified": True,
            "otp": None
        }).eq("id", user['id']).execute()
        
        return {"message": "Email verified successfully!"}
        
    except Exception as e:
        print("Error:", str(e))  # Add debug logging
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/resend-otp")
async def resend_otp():
    try:
        # Generate new 6-digit OTP
        new_otp = str(randint(100000, 999999))
        
        # Get user from session or token (you'll need to implement this)
        # For now, this is a placeholder
        # user = get_current_user()
        
        # Update user's OTP in database
        # supabase.table("users").update({"otp": new_otp}).eq("email", user.email).execute()
        
        # Send new OTP email
        # message = MessageSchema(
        #     subject="New Verification Code",
        #     recipients=[user.email],
        #     body=f"""
        #     Your new verification code is: {new_otp}
        #     
        #     This code will expire in 5 minutes.
        #     """,
        #     subtype="html"
        # )
        
        # fm = FastMail(conf)
        # await fm.send_message(message)
        
        return {"message": "New OTP sent successfully"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Login Route
@app.post("/login")
async def login(user: UserLogin):
    # Fetch user from Supabase
    response = supabase.table("users").select("*").eq("email", user.email).execute()
    user_data = response.data
    if not user_data:
        raise HTTPException(status_code=400, detail="User not found")

    user_info = user_data[0]

    # Check if user is verified
    if not user_info["is_verified"]:
        raise HTTPException(status_code=400, detail="Email not verified")

    # Validate password
    if not pwd_context.verify(user.password, user_info["password"]):
        raise HTTPException(status_code=400, detail="Incorrect password")

    # Generate JWT Token
    token = jwt.encode({"email": user.email}, SECRET_KEY, algorithm="HS256")

    return {"message": "Login successful", "token": token}
