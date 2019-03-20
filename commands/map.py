from sqlalchemy.orm import sessionmaker

from common.database import db_engine
from common.world import world, get_tile_id, get_tile, get_local_area
from models.player import Player
from models.tile import Tile


def _emojify_area(area, player, session):
    result = ""
    for x, x_chunk in enumerate(area['tiles']):
        for y, tile_id in enumerate(x_chunk):
            tile = get_tile(tile_id, session)
            new_x = area['x'] + x
            new_y = area['y'] + y
            if player.x == new_x and player.y == new_y:
                result += "❌"
            else:
                result += tile.display_emoji
        result += "\n"
    return result


def run_command(message):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.id == message.author.id).first()

    local_area = get_local_area(player.x, player.y)

    current_tile_id = get_tile_id(player.x, player.y)
    current_tile = get_tile(current_tile_id, session)

    result = _emojify_area(local_area, player, session)
    result += f"`> you are at x: {player.x}, y: {player.y} ({current_tile.name})`"
    return result
