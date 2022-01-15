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
    children = relationship('Posts', backref='author',cascade="all, delete",passive_deletes=True)

class Posts(base):
    __tablename__ = 'posts123'
    id = Column(Integer(), primary_key=True)
    title = Column(String(length=100), nullable=False)
    description = Column(TEXT(charset='latin1'), nullable=False)
    user_id = Column(Integer, ForeignKey('users123.id', ondelete="CASCADE"))

    # if we access the user via post table then
    # post = session.query(Posts).filter(Post.id == 1).first()
    # print(post.author)

    # if we want to access user by User table then
    # user = session.query(User).filter(User.id == 1).first()
    # print(user.username)


# class Parent(base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child")
#
# class Child(base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))