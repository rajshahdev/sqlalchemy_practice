from main import SessionLocal, engine
from models import User, Posts

local_session = SessionLocal(bind=engine)
new_user = User(username = 'rajshaasaasash', email='rajshaaasssah@gmail.com')
diff_user = User(username = 'xoxo', email='xoxo@xoxo.com')
new_post = Posts(title = 'rahbkbkadb dsajbdk asjkdb', description = 'ajbskabsa asbkbakbskas bkjasbajabskjabkjabkas jabskjbasjbajsbkasababskbskakbaksba kjbaskjbakbaskjbaksbkabska kjabskjabkbsakjbkabska kjabskasbajksbak')
# local_session.add(new_user)
# local_session.commit()

local_session.add(diff_user)
local_session.commit()

# local_session.add(new_post)
# local_session.commit()