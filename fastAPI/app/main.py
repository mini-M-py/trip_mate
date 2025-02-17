from fastapi import  FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
import jwt
from dotenv import load_dotenv
import secrets
from . import model
from .database import engine, supabase
from .routers import user

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your Next.js frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)

model.Base.metadata.create_all(bind=engine)
#createBucket("Bucket")

secret_key = secrets.token_hex(32) 

load_dotenv()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Store OTPs temporarily
otp_store = {}

# JWT Secret Key
SECRET_KEY=secret_key

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class OTPVerification(BaseModel):
    otp: int

# Signup Route

@app.get("/")
async def root():
    return {"message": "Hello World"}

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
