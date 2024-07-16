from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "full_name": "example",
                "email": "example@gmail.com",
                "password": "admin"
            }
        }
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "example@gmail.com",
                "password": "admin"
            }
        }

class PostSchema(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    author: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "A",
                "description": "v",
                "author": "b"
            }
        }