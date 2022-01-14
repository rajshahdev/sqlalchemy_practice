from sqlalchemy import create_engine, Table, Integer,String, Column,MetaData,insert,func,ForeignKey
from sqlalchemy import text
engine = create_engine('sqlite:///college.db', echo = True)

meta = MetaData()
conn = engine.connect()
students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)
from sqlalchemy.sql import select
from sqlalchemy import and_
stmt = select([students]).where(and_(students.c.name == 'Ravi'))
result = conn.execute(stmt)
print (result.fetchall())
