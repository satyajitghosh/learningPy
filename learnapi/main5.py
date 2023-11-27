'''
Same as the last file.
Except this time the app is connected to a database.
'''
from fastapi import FastAPI,status,HTTPException
from fastapi.responses import Response
from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import db

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool = True


@app.get("/posts")
def posts():
    posts = db.sqlquery("""select * from posts""")
    return {"data":posts}

@app.get("/posts/latest")
def get_post():
    sql = """
    select * from posts p,
    (
        select max(id) as id from posts 
    )m 
    where p.id = m.id
    """ 
    post = db.sqlquery(sql)
    return {"data":post}

@app.get("/posts/{id}")
def get_post(id:int):
    post = db.sqlquery("""select * from posts where id =  %s """,(str(id)))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found.")
    return {"data":post}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    post = db.sqlquery("""insert into posts (title,content,published) values (%s,%s,%s) returning * """,(post.title,post.content,post.published))
    return {"data":post}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    deleted_post = db.sqlquery("""delete from posts where id = %s returning * """,(str(id)))
    if len(deleted_post) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} does not exist.")

@app.put("/posts/{id}")
def update_post(id:int,new_post:Post):
    
    updated_post = db.sqlquery("""
                               update posts
                               set
                               title = %s,
                               content = %s,
                               published = %s
                               where id = %s
                               returning * 
                               """,(new_post.title,new_post.content,new_post.published,id))
    if len(updated_post)==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} does not exist.")

    return {"message":updated_post}