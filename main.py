from fastapi import FastAPI,Depends
from database import Engine,get_db
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models
import post

models.Base.metadata.create_all(bind=Engine)

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_posts(db: Session =Depends(get_db)):
    posts =db.query(models.Post).all()
    return posts

app.include_router(post.router)

