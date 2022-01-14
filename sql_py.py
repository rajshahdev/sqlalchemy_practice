from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData


# to connect with mysql localhost the below syntax
# engine = create_engine("mysql+pymysql://root:@Techraj1@localhost/raj_db?host=localhost?port=3306", echo=True)

# to directly create a db file
engine = create_engine("sqlite:///college.db", echo=True)
con = engine.connect()

print(con)
# Method & Description
# 1	connect():-Returns connection object
#
# 2	execute():-Executes a SQL statement construct
#
# 3	begin():- Returns a context manager delivering a Connection with a Transaction established. Upon successful
# operation, the Transaction is committed, else it is rolled back
#
# 4	dispose():-Disposes of the connection pool used by the Engine
#
# 5	driver():-Driver name of the Dialect in use by the Engine
#
# 6	table_names():-Returns a list of all table names available in the database
#
# 7	transaction():-Executes the given function within a transaction boundary

# the below is the meta constructor which we use to create a table in alchemy

meta = MetaData()

students = Table('students',meta,
                 Column('id',Integer,primary_key=True),
                 Column('name',String),
                 Column('lastname',String),
                 )

# after creating the table we then write create_all to store all the info's to the metadata.
meta.create_all(engine)

# for single insert

# ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
# ins = students.insert().values(name = 'Raviya', lastname = 'Kapoora')
# con.execute(ins)

# for bulk insert

# con.execute(students.insert(), [
#    {'name':'Rajiv', 'lastname' : 'Khanna'},
#    {'name':'Komal','lastname' : 'Bhandari'},
#    {'name':'Abdul','lastname' : 'Sattar'},
#    {'name':'Priya','lastname' : 'Rajhans'},
# ])

# select query in sqlalchemy

# s = students.select()
# for i in con.execute(s):
#     print(i)

# select with specific condition
# s = students.select().where(students.c.id>2)
# here 'c' is refers to column attribute
# for i in con.execute(s):
#     print(i)

# select is also a function of sqlalchemy.sql
# from sqlalchemy.sql import select
# s = select([students])
# result = con.execute(s)
# for i in result:
#     print(i)

# now if you want to pass the same query just like mysql then you've to use text from sqlalchemy
from sqlalchemy import text
t = text("SELECT * FROM students")
result = con.execute(t)
for i in result:
    print(i)