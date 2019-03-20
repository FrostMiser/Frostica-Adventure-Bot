import random
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker

from common.database import db_engine
from models.item import Item
from models.player import Player
from models.player_inventory import PlayerInventory


def run_command(message, message_content):
    item_name = ' '.join(message_content.split(" ")[1:]) if len(message_content.split(" ")) > 1 else None
    if item_name:
        session_maker = sessionmaker(bind=db_engine)
        session = session_maker()
        player = session.query(Player).filter(Player.id == message.author.id).first()

        item_lookup_result = session.query(Item).filter(Item.name == item_name).first()
        if item_lookup_result:
            player_inventory = session.query(PlayerInventory).filter(
                and_(
                    PlayerInventory.player_id == message.author.id,
                    PlayerInventory.item_id == item_lookup_result.id)
            ).first()
            if player_inventory:
                if player_inventory.item.edible:
                    response = _eat_item(player, player_inventory, session)
                else:
                    response = 'You aren\'t sure how to use this item.'
            else:
                response = 'You don\'t seem to have that item.'
        else:
            response = 'That item does not exist.'
    else:
        response = 'You must say which item you want to use with !use <item>.'
    return response


def _eat_item(player, player_inventory, session):
    if player.hunger < player.max_hunger:
        item_name = player_inventory.item.name
        if player_inventory.item.hunger_satisfaction + player.hunger > player.max_hunger:
            player.hunger = player.max_hunger
        else:
            player.hunger = player_inventory.item.hunger_satisfaction + player.hunger
        if player_inventory.item_amount == 1:
            session.delete(player_inventory)
        else:
            player_inventory.item_amount -= 1
        session.commit()
        response = 'You eat the {} and feel less hungry.'.format(item_name)
    else:
        response = 'You aren\'t hungry.'
    return response
