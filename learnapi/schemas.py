from pydantic import BaseModel,EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True

class PostCreate(PostBase):
    pass

# Why orm_mode = True? The DB returns the post in the form of an ORM Model and not a dictionary - which a pydantic model
# readily recognizes. When  orm_mode = True is set, Pydantic converts the ORM model to dictionary to check.
 
class Post(PostBase):
    # This inherits PostBase whic already has title,content,and published fields.
    # In addition Post will have the id and created_at fields.
    id:int
    created_at:datetime
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    user:EmailStr
    password:str
    
class UserOut(BaseModel):
    id:int
    user:EmailStr
    created_at:datetime
    class Config:
        orm_mode = True