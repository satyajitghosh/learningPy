from fastapi import FastAPI,status,HTTPException,Depends,APIRouter
from fastapi.responses import Response
from sqlalchemy.orm import Session
from .. import models,schemas,utils
from ..dbalchemy import get_db
from typing import List

router = APIRouter(prefix="/posts",tags=["Posts"])
# tags helps with segregating the endpoints in the HTML docs.

@router.get("/",response_model=List[schemas.Post])
def posts(db:Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@router.get("/{id}",response_model=schemas.Post)
def get_post(id:int,db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found.")
    return post

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db:Session = Depends(get_db)):
    new_post = models.Post(title=post.title,content=post.content,published=post.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} does not exist.")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db:Session = Depends(get_db)):
    
    post_query = db.query(models.Post).filter(models.Post.id==id)
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} does not exist.")
    
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    
    return post_query.first()

