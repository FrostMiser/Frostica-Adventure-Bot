import random

from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from models.player import Player
from models.item import Item
from models.player_inventory import PlayerInventory


def run_command(db_engine, message, message_content):
    item_name = message_content.split(" ")[1:] if len(message_content.split(" ")) > 1 else None

    if item_name:
        session_maker = sessionmaker(bind=db_engine)
        session = session_maker()

        item_lookup_result = session.query(Item).filter(Item.name == item_name).first()
        if item_lookup_result:
            player_inventory = session.query(PlayerInventory).filter(
                and_(
                    PlayerInventory.player_id == message.author.id,
                    PlayerInventory.item_id == item_lookup_result.id)
            ).first()
            if player_inventory:
                if player_inventory.item_amount == 1:
                    session.delete(player_inventory)
                else:
                    player_inventory.item_amount -= 1
                response = 'You use your item.'
                session.commit()
            else:
                response = 'You don\'t seem to have that item.'
        else:
            response = 'That item does not exist.'
    else:
        response = 'You must say which item you want to use with !use <item>.'
    return response
