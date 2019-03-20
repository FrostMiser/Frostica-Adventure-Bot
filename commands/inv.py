from sqlalchemy.orm import sessionmaker

from common.database import db_engine
from models.item import Item
from models.player import Player
from models.player_inventory import PlayerInventory


# ToDo Add the ability to scroll inventory for when there is a long list
# ToDo Add the ability to search/filter inventory, maybe a way to filter by edible items?
def run_command(message):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.id == message.author.id).first()
    response = '__:baggage_claim: {}\'s Inventory__'.format(player.name)
    for inventory_item in player.inventory:
        response += '\n{}({})'.format(inventory_item.item.name, inventory_item.item_amount)
    return response
