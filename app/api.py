from fastapi import FastAPI, Body, Depends

from app.auth.auht_bearer import JWTBearer
from app.auth.auht_handler import sign_jwt
from app.model import PostSchema, UserSchema, UserLoginSchema

posts = [
    {
        'id': 1,
        'title': 'Pancake',
        'content': 'Lorem Ipsum ...'
    }
]

users = []

app = FastAPI()


@app.get('/', tags=['root'])
async def read_root() -> dict:
    return {'message': 'Welcome to your blog!.'}


@app.get('/post', tags=['posts'])
async def get_posts() -> dict:
    return {'data': posts}


@app.get('/post/{id}', tags=['posts'])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            'error': 'No such post with the supplied ID.'
        }

    for post in posts:
        if posts['id'] == id:
            return {
                'data': post
            }


@app.post('/user/signup', tags=['user'])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)  # replace with db call, making sure to hash the password first
    return sign_jwt(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.post('/user/login', tags=['user'])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return sign_jwt(user.email)
    return {
        'error': 'Wrong login details!'
    }


@app.post('/posts', dependencies=[Depends(JWTBearer())], tags=['post'])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        'data': 'post added.'
    }
