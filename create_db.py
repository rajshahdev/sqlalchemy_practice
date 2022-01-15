from main import base, engine
from models import User, Posts
base.metadata.create_all(engine)