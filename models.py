from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, UniqueConstraint
from sqlalchemy.dialects.mysql import TEXT
from main import base
from sqlalchemy.orm import relationship, backref



class User(base):
    __tablename__ = 'trusers'
    id = Column(Integer(), primary_key=True)
    username = Column(String(length=30), nullable=False, unique=True)
    email = Column(String(length=30), nullable=False, unique=True)
    created_at = Column(DateTime(), server_default='now()')
    child = relationship('Posts', back_populates='parent', uselist=False)

class Posts(base):
    __tablename__ = 'trposts'
    id = Column(Integer(), primary_key=True)
    title = Column(String(length=100), nullable=False)
    description = Column(TEXT(charset='latin1'), nullable=False)
    user_id = Column(Integer, ForeignKey('trusers.id'), unique=True)
    parent = relationship('User',back_populates='child')



# class Parent(base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child")
#
# class Child(base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))