from pydantic import BaseModel, Field


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
