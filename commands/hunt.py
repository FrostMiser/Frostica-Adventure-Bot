import random

from sqlalchemy.orm import sessionmaker
from models.player import Player
from models.item import Item
from models.player_inventory import PlayerInventory
from common.database import db_engine


def run_command(message):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.id == message.author.id).first()

    item_lookup_results = session.query(Item).filter(Item.hunt_drop_chance > 0).all()
    possible_items = {item.id: item.hunt_drop_chance for item in item_lookup_results}

    hunted_item_id = random.choices(list(possible_items.keys()), possible_items.values())[0]
    hunted_item = session.query(Item).filter(Item.id == hunted_item_id).first()

    player_inventory = session.query(PlayerInventory).filter(PlayerInventory.item_id == hunted_item.id).first()

    if player_inventory:
        player_inventory.item_amount += 1
    else:
        player.inventory.append(PlayerInventory(player_id=player.id, item_id=hunted_item.id, item_amount=1))
    session.commit()
    response = '{} went hunting and found a {}'.format(player.name, hunted_item.name)
    return response
