from main import SessionLocal, engine
from models import User, Posts

local_session = SessionLocal(bind=engine)

users = local_session.query(User).all()[:2]
for i in users:
    print(i.username)
    print(i.email)

users = local_session.query(User).filter(User.username == 'rajshah').first()
print(users)
# for i in users:
#     print(i.email)