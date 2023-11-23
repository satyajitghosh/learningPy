## Some basic differences between get and post.
'''
Get
---
Sends data through URL
Not secured as the data is visible in the URL
Can send less data through the get request
Get request can be cached
Can be bookmarked

Post
----
Sends data through the body of the request
Comapritively more secured as the data is not visible in the URL
Can send more data through the post request
Post request cannot be cached
Cannot be bookmarked

Pydantic Model of Post 
----------------------
This ensures that the blog post passed to the API function post
must be in a particular format - ie. it must have the non-optional
fields - title and content.

'''
from fastapi import FastAPI
from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating:Optional[int] = None

@app.get("/")
def root():
    return {"Message":"Hello World."}

@app.get("/posts")
def geet_posts():
    return {"data":"This is your posts."}

@app.post("/createposts")
def create_posts(post:Post):
    print(post)
    print(post.dict())
    return {"new_post":"New"}