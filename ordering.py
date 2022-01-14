from main import SessionLocal, engine
from models import User, Posts
from sqlalchemy import desc

local_session = SessionLocal(bind=engine)

# for ascending order
users = local_session.query(User).order_by(User.username).all()
#

# for descending order
users = local_session.query(User).order_by(desc(User.username)).all()

for user in users:
    print(user.username)
