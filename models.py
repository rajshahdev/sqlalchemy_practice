from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.dialects.mysql import TEXT
from main import base
from sqlalchemy.orm import relationship



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



# class Parent(base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child")
#
# class Child(base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))
