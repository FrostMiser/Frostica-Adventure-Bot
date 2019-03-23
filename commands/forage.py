import random

from models.item import Item
from models.player import Player
from models.player_inventory import PlayerInventory
from common.world import get_tile_from
from common.helpers import drain_player_hunger_and_thirst, get_hunger_and_thirst_warnings


def run_command(message, session):
    player = session.query(Player).filter(Player.id == message.author.id).first()

    tile = get_tile_from(player.x, player.y, session)
    if not tile.can_forage:
        response = 'You didn\'t find anything here, maybe try somewhere else.'
    else:
        item_lookup_results = session.query(Item).filter(Item.forage_drop_chance > 0).all()
        possible_items = {item.id: item.forage_drop_chance for item in item_lookup_results}

        foraged_item_id = random.choices(list(possible_items.keys()), possible_items.values())[0]
        foraged_item = session.query(Item).filter(Item.id == foraged_item_id).first()

        player_inventory = session.query(PlayerInventory).filter(PlayerInventory.item_id == foraged_item.id).first()
        drain_player_hunger_and_thirst(player)

        if player_inventory:
            player_inventory.item_amount += 1
        else:
            player.inventory.append(PlayerInventory(player_id=player.id, item_id=foraged_item.id, item_amount=1))
        response = '{} went foraging and found a {}'.format(player.name, foraged_item.name)
        response += get_hunger_and_thirst_warnings(player)
    return response
