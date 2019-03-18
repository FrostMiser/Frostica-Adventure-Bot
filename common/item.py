from sqlalchemy.orm import sessionmaker
from models.player import Player
from models.item import Item
from models.player_inventory import PlayerInventory
from common.database import db_engine

def get_item(name):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    item = session.query(Item).filter(Item.name == name).first()
    session.expunge(item)
    session.close()
    return item
