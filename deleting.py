from main import SessionLocal, engine
from models import User, Posts

local_session = SessionLocal(bind=engine)

user_to_delete = local_session.query(User).filter(User.username == 'xoxo').first()
local_session.delete(user_to_delete)
local_session.commit()