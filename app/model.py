from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'title': 'Securing FastAPI applications with JWT.',
                'content': 'In this tutorial, you will learn how to secure you application using JWT. We will be using PyJWT to sign, encode and decode JWT tokens...'
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'fullname': 'Vasiliy Vladimirovich Pupkin',
                'email': 'vasya@mail.ru',
                'password': 'weakpassword'
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'email': 'vasya@mail.ru',
                'password': 'weakpassword'
            }
        }
