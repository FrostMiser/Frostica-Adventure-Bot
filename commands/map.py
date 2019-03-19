import random

from sqlalchemy.orm import sessionmaker
from models.player import Player
from models.tile import Tile
from models.player_inventory import PlayerInventory
from common.database import db_engine

world = {
  'x':0,
  'y':0,
  'tiles': [
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,3,0,0,0],
    [0,1,1,1,1,0,1,0,0,0],
    [0,0,0,1,1,1,1,0,0,0],
    [0,3,0,1,1,1,1,0,3,0],
    [0,0,0,1,1,1,1,3,0,0],
    [0,3,0,3,3,1,3,0,0,0],
    [0,2,2,0,3,1,1,3,0,0],
    [0,2,2,0,0,1,0,3,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,3,0,0,0],
    [0,1,1,1,1,0,1,0,0,0],
    [0,0,0,1,1,1,1,0,0,0],
    [0,3,0,1,1,1,1,0,3,0],
    [0,0,0,1,1,1,1,3,0,0],
    [0,3,0,3,3,1,3,0,0,0],
    [0,2,2,0,3,1,1,3,0,0],
    [0,2,2,0,0,1,0,3,0,0],
    [0,0,0,0,0,0,0,0,0,0]
  ]
}

def emojify_area(area, player, session):
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

def get_tile_id(x, y):
  if(y < 0 or x < 0):
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

def get_local_area(player, limit = 5):
  negative_offset_x = player.x - limit
  negative_offset_y = player.y - limit

  positive_offset_x = player.x + limit
  positive_offset_y = player.y + limit

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

def run_command(message, message_content):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.id == message.author.id).first()

    local_area = get_local_area(player)

    current_tile_id = get_tile_id(player.x, player.y)
    current_tile = get_tile(current_tile_id, session)

    result = emojify_area(local_area, player, session)
    result += f"\nyou are at x: {player.x}, y: {player.y} ({current_tile.name})"
    return result