'''
This uses the ORM sqlalchemy to connect and transact with the database,
thus removing the need to use SQL statements.

Note - 
Pydantic models are used to enforce a structure in the request and response.
ORM models are used to interact with the database.

Pydantic models are defined in schemas.py
ORM Models are defined in the models.py
'''
from fastapi import FastAPI
from . import models
from .dbalchemy import engine

from .routers import post,user,auth,votes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)



