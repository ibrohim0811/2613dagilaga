from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    language_code: Optional[str] = "uz"
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    telegram_id: int
    

    