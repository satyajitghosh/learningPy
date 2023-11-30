from .dbalchemy import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,server_default='TRUE',default=True)
    created_at = Column(TIMESTAMP,nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    # Note - the following is not a column. It is a relationship
    # The model sends the relevant record in the user table when it is queried. 
    owner=relationship("User")
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,nullable=False)
    user = Column(String,unique=True,nullable=False)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP,nullable=False,server_default=text('now()'))

class Vote(Base):
    __tablename__ = "votes"
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)

    
