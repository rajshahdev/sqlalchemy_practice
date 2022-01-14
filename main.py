from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

base = declarative_base()

engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/fastapi')

SessionLocal = sessionmaker()


# class User(base):
#     __tablename__ = 'users123'
#     id = Column(Integer(), primary_key=True)
#     username = Column(String(length=30), nullable=False, unique=True)
#     email = Column(String(length=30), nullable=False, unique=True)
#     created_at = Column(DateTime(), server_default='now()')

    
