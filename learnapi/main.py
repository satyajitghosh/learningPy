## Start the API using uvicorn. Command below.
## uvicorn main:app --reload
## reload options ensures that the server is restarted after changes to a file are saved.
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Message":"Hello World."}

@app.get("/posts")
def geet_posts():
    return {"data":"This is your posts."}

