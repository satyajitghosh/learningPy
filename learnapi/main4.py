## Some basic differences between get and post.
'''
Errors and response status codes.
Exploring proper ways to pass status/response codes.

Documentation links - 
---------------------
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

'''
from fastapi import FastAPI,status,HTTPException
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

def find_index(id:int):
    for i,post in enumerate(my_posts):
        if id==post['id']:
            return i

@app.get("/posts")
def posts():
    return {"data":my_posts}

@app.get("/posts/latest")
def get_post():
    post = my_posts[-1]
    return {"data":post}

@app.get("/posts/{id}")
def get_post(id:int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found.")
    return {"data":post}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(1,10000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index = find_index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} does not exist.")
    my_posts.pop(index)

@app.put("/posts/{id}")
def update_post(id:int,updated_post:Post):
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} does not exist.")
    updated_post = updated_post.dict()
    updated_post['id'] = id 
    my_posts[index] = updated_post
    return {"message":updated_post}