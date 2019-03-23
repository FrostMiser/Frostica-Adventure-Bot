from common.world import get_tile, get_tile_id, get_tile_from
from models.player import Player
from common.helpers import drain_player_hunger_and_thirst, get_hunger_and_thirst_warnings


def _move(player, session, x=0, y=0):
    tile_moving_to = get_tile_from(player.x + x, player.y + y, session)
    drain_player_hunger_and_thirst(player, tile_moving_to.hunger_drain_amount, tile_moving_to.thirst_drain_amount)
    traversable = tile_moving_to.traversable
    if traversable:
        player.x += x
        player.y += y
    return traversable


direction_dict = {
    'north': [0, -1],
    'n': [0, -1],
    'south': [0, 1],
    's': [0, 1],
    'east': [1, 0],
    'e': [1, 0],
    'west': [-1, 0],
    'w': [-1, 0]
}


def _move_direction(player, session, direction):
    if _move(player, session, *direction_dict[direction]):
        return f"you move {direction}\n"
    else:
        x, y = direction_dict[direction]
        return f"you can't traverse (move over) {get_tile_from(player.x + x, player.y + y, session).name}\n"


def run_command(message, message_content, session):
    player = session.query(Player).get(message.author.id)

    direction = ''.join(message_content.split(" ")[1:]) if len(message_content.split(" ")) > 1 else None

    if direction in direction_dict:
        response = _move_direction(player, session, direction)
    else:
        return ("You must say which direction you want to use with !use <direction>.\n"
                "valid directions are north, east, south, and west.")

    current_tile_id = get_tile_id(player.x, player.y)
    current_tile = get_tile(current_tile_id, session)

    response += f"`> you are at x: {player.x}, y: {player.y} ({current_tile.name})`"
    response += get_hunger_and_thirst_warnings(player)
    return response
