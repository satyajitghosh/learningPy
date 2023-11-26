from dbalchemy import Base
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,server_default='TRUE',default=True)
    created_at = Column(TIMESTAMP,nullable=False,server_default=text('now()'))
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,nullable=False)
    user = Column(String,unique=True,nullable=False)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP,nullable=False,server_default=text('now()'))

    
