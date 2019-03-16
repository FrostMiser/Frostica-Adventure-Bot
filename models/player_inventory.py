from common.base import Base
from models.player import Player
from models.item import Item

from sqlalchemy import Column, Integer, String, UniqueConstraint


class PlayerInventory(Base):
    __tablename__ = 'player_inventory'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey(Player.id))
    item_id = Column(Integer, ForeignKey(Item.id))
    item_amount = Column(Integer)
    UniqueConstraint('player_id', 'item_name')
