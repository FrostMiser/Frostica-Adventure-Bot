from sqlalchemy.orm import sessionmaker

from common.database import db_engine
from models.item import Item
from models.player import Player
from models.player_inventory import PlayerInventory
from models.recipe_ingredient import RecipeIngredient

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


def get_item_by_name(name, session):
    item = session.query(Item).filter(Item.name == name).first()
    return item
