from sqlalchemy.orm import sessionmaker

from models.player import Player
from models.item import Item
from models.player_inventory import PlayerInventory
from models.recipe_ingredient import RecipeIngredient
from common.database import db_engine
'''
This file contains helpers for making it easier to get data and do other things. 

Function Naming:
    get_something() - Lookup something by it's name
    get_something_by_specifier() - Lookup by something other than name
    
    If the something portion is pluralized, it is expected that the function can return multiple values
'''


def get_session():
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    return session


def get_item(name):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    item = session.query(Item).filter(Item.name == name).first()
    session.expunge(item)
    session.close()
    return item
