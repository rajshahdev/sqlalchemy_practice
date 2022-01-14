from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.mysql import TEXT
from main import base




class User(base):
    __tablename__ = 'users123'
    id = Column(Integer(), primary_key=True)
    username = Column(String(length=30), nullable=False, unique=True)
    email = Column(String(length=30), nullable=False, unique=True)
    created_at = Column(DateTime(), server_default='now()')

class Posts(base):
    __tablename__ = 'posts123'
    id = Column(Integer(), primary_key=True)
    title = Column(String(length=100), nullable=False)
    description = Column(TEXT(charset='latin1'), nullable=False)
