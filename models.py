from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from database import Base

class Post(Base):
    __tablename__="posts"

    Id=Column(Integer,primary_key=True,autoincrement=True)
    Title=Column(String,nullable=True)
    Content=Column(String,nullable=True)

