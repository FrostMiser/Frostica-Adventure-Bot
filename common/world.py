from models.player import Player
from models.tile import Tile
from common.database import db_engine

# TILE REFERENCE
# 0 = mountains
# 1 = flat snow
# 2 = water
# 3 = trees

world = {
    'x': 0,
    'y': 0,
    'tiles': [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 3, 0, 1, 1, 1, 1, 0, 3, 0],
        [0, 0, 0, 1, 1, 1, 1, 3, 0, 0],
        [0, 3, 0, 3, 3, 1, 3, 0, 0, 0],
        [0, 2, 2, 0, 3, 1, 1, 3, 0, 0],
        [0, 2, 2, 0, 0, 1, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 3, 0, 1, 1, 1, 1, 0, 3, 0],
        [0, 0, 0, 1, 1, 1, 1, 3, 0, 0],
        [0, 3, 0, 3, 3, 1, 3, 0, 0, 0],
        [0, 2, 2, 0, 3, 1, 1, 3, 0, 0],
        [0, 2, 2, 0, 0, 1, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
}


def get_tile_id(x, y):
    if y < 0 or x < 0:
        tile_id = -1
    else:
        try:
            world_y = world['tiles'][y]
            tile_id = world_y[x]
        except (ValueError, IndexError, KeyError) as e:
            tile_id = -1
    return tile_id


def get_tile(id, session):
    return session.query(Tile).get(id)


def get_tile_from(x, y, session):
    tile_id = get_tile_id(x, y)
    return get_tile(tile_id, session)


def get_local_area(pos_x, pos_y, limit=5):
    negative_offset_x = pos_x - limit
    negative_offset_y = pos_y - limit

    positive_offset_x = pos_x + limit
    positive_offset_y = pos_y + limit

    local_area = {
        'x': negative_offset_x,
        'y': negative_offset_y,
        'tiles': []
    }
    for y in range(negative_offset_y, positive_offset_y):
        y_chunk = []
        for x in range(negative_offset_x, positive_offset_x):
            tile_id = get_tile_id(x, y)
            y_chunk.append(tile_id)
        local_area['tiles'].append(y_chunk)
    return local_area
