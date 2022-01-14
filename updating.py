from main import SessionLocal, engine
from models import User, Posts

local_session = SessionLocal(bind=engine)

user_to_update = local_session.query(User).filter(User.username=='rajshah').first()
user_to_update.username = 'raj'
user_to_update.email = 'raj@shah.com'
local_session.commit()