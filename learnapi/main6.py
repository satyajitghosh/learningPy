'''
This uses the ORM sqlalchemy to connect and transact with the database,
thus removing the need to use SQL statements.

Note - 
Pydantic models are used to enforce a structure in the request and response.
ORM models are used to interact with the database.

Pydantic models are defined in schemas.py
ORM Models are defined in the models.py
'''
from fastapi import FastAPI,status,HTTPException,Depends
from fastapi.responses import Response
from typing import Optional,List
from fastapi.params import Body
from random import randrange
from sqlalchemy.orm import Session
import models,schemas,utils
from dbalchemy import engine,get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/posts",response_model=List[schemas.Post])
def posts(db:Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.get("/posts/{id}",response_model=schemas.Post)
def get_post(id:int,db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found.")
    return post

@app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db:Session = Depends(get_db)):
    new_post = models.Post(title=post.title,content=post.content,published=post.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} does not exist.")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db:Session = Depends(get_db)):
    
    post_query = db.query(models.Post).filter(models.Post.id==id)
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} does not exist.")
    
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    
    return post_query.first()

@app.post("/users/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/{id}",response_model=schemas.UserOut)
def get_user(id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post with id {id} not found.")
    return user
