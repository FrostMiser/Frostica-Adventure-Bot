from common.base import Base
from models.player import Player

from sqlalchemy import Column, Integer, String


class PlayerInventory(Base):
    __tablename__ = 'player_inventory'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey(Player.id))
    item_name = Column(String)
    item_amount = Column(Integer)
