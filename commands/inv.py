from sqlalchemy.orm import sessionmaker
from models.player import Player
from models.item import Item
from models.player_inventory import PlayerInventory


def run_command(db_engine, message):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.id == message.author.id).first()
    response = '__{}\'s Inventory__'.format(player.name)
    for inventory_item in player.inventory:
        response += '\n{}({})'.format(inventory_item.item.name, inventory_item.item_amount)
    return response
