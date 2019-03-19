import random

from sqlalchemy.orm import sessionmaker
from models.player import Player
from models.block import Block
from models.player_inventory import PlayerInventory
from common.database import db_engine

world = [
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

def emojify_area(area, session):
  result = ""
  for x_chunk in area:
    for block_id in x_chunk:
      block = session.query(Block).filter(Block.id == block_id).first()
      result += block.display_emoji
    result += "\n"
  return result

def run_command(message, message_content):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.id == message.author.id).first()

    return emojify_area(world, session)