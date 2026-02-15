from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.user_storage import create_user, authenticate_user
from app.core.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


@router.post("/register")
def register(user: UserCreate):
    create_user(user.username, user.password)
    return {"message": "User created successfully"}


@router.post("/login")
def login(user: UserLogin):
    authenticated_user = authenticate_user(user.username, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": authenticated_user.username})
    return {"access_token": token, "token_type": "bearer"}
