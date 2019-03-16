from common.base import Base

from common.base import Base
from sqlalchemy.orm import sessionmaker
from models.player import Player

# ToDo Make this not runnable, or have some kind of permission on it
def run_command(db_engine):
    Base.metadata.drop_all(bind=db_engine)
    response = 'Database cleared.'
    return response
