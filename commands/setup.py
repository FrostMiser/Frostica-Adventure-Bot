from sqlalchemy.orm import sessionmaker

from common.base import Base
from models.item import Item


def run_command(db_engine):
    _populate_items()
    response = 'Setup complete.'
    return response


def _populate_items(db_engine):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    session.add(Item(name='Stone', description='A small stone.'))
    session.commit()
