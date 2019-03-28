"""
This file contains helpers for making it easier to get data and do other things.

Function Naming:
    get_something() - Lookup something by it's name
    get_something_by_specifier() - Lookup by something other than name

    If the something portion is pluralized, it is expected that the function can return multiple values
"""

import re

from sqlalchemy.orm import sessionmaker

from common.database import db_engine
from models.item import Item
from models.player_inventory import PlayerInventory
from models.player import Player

def get_session():
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    return session


def get_player(session, player_id):
    return session.query(Player).get(player_id)


def get_item_by_name(name, session):
    item = session.query(Item).filter(Item.name == name).first()
    return item


def drain_player_hunger_and_thirst(player, hunger_amount=1, thirst_amount=1):
    if player.hunger > 0:
        player.hunger = max(player.hunger - hunger_amount, 0)
    else:
        if player.health > 0:
            player.health -= 1
    if player.thirst > 0:
        player.thirst = max(player.thirst - thirst_amount, 0)
    else:
        if player.health > 0:
            player.health -= 1


def get_hunger_and_thirst_warnings(player):
    response = ''
    if player.thirst == 0:
        response += '\n:warning: {} is thirsty.'.format(player.name)
    if player.hunger == 0:
        response += '\n:warning: {} is hungry.'.format(player.name)
    return response


# Code that gets run upon the completion of commands
def complete_command(player, session):
    response = ''
    if player.hunger == 0 or player.thirst == 0:
        if player.health == 0:
            if player.thirst == 0:
                message = '{} died of thirst.️'.format(player.name)
            else:
                message = '{} died of hunger️r'.format(player.name)
            message_dashes = re.sub('.', '-', message)
            response = '\n☠️\n`{message_dashes}`\n`{message}`\n`{message_dashes}`\n☠️\n'.format(message_dashes=message_dashes, message=message)
            _reset_player(player, session)
    return response


def _reset_player(player, session):
    player_id = player.id
    # ToDo Add the ability for certain items to persist, also need to check player equipment
    player_inventory = session.query(PlayerInventory).filter(PlayerInventory.player_id == player_id).all()
    for player_inventory_item in player_inventory:
        session.delete(player_inventory_item)
    session.delete(player)
