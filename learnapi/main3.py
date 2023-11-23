## Some basic differences between get and post.
'''
In this file, we see how to implement these functionalities with an actual post,
that we store in some variables. 

We dont use database yet.

Note - Ordering matters.
@app.get("/posts/latest") should apear before @app.get("/posts/{id}")
Why?  The control will try to match the URL - first with the method - get/post,
then with the first part of the URL 'posts',
and then with the second part. If "/posts/{id}" appears first in order, it might try to match
'latest' with "/posts/{id}" and try to convert 'latest' to integer and fail.
'''
from fastapi import FastAPI,status
from fastapi.responses import Response
from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating:Optional[int] = None

my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},
            {"title":"favourite foods","content":"I love Pizza","id":2}]

def find_post(id:int):
    for post in my_posts:
        if id==post['id']:
            return post

@app.get("/posts")
def posts():
    return {"data":my_posts}

@app.get("/posts/latest")
def get_post():
    post = my_posts[-1]
    return {"data":post}

@app.get("/posts/{id}")
def get_post(id:int,response:Response):
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":f"Post with ID {id} not found."}
    return {"data":post}

@app.post("/posts")
def create_posts(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(1,10000000)
    my_posts.append(post_dict)
    return {"data":post_dict}