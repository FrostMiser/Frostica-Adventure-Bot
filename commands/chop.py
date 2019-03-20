import random
from sqlalchemy.orm import sessionmaker

from common.database import db_engine
from models.item import Item
from models.player import Player
from models.player_inventory import PlayerInventory
from common.world import get_tile_from

def run_command(message):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.id == message.author.id).first()

    tile = get_tile_from(player.x, player.y, session)
    if not tile.can_chop:
        response = 'You didn\'t find anything here, maybe try somewhere else.'
    else:
        item_lookup_results = session.query(Item).filter(Item.chop_drop_chance > 0).all()
        possible_items = {item.id: item.chop_drop_chance for item in item_lookup_results}

        chopped_item_id = random.choices(list(possible_items.keys()), possible_items.values())[0]
        chopped_item = session.query(Item).filter(Item.id == chopped_item_id).first()

        player_inventory = session.query(PlayerInventory).filter(PlayerInventory.item_id == chopped_item.id).first()

        if player_inventory:
            player_inventory.item_amount += 1
        else:
            player.inventory.append(PlayerInventory(player_id=player.id, item_id=chopped_item.id, item_amount=1))
        session.commit()
        response = ':evergreen_tree: {} chopped a tree and found a {}'.format(player.name, chopped_item.name)
    return response
