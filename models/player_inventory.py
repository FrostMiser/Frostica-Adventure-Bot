from sqlalchemy import Column, Integer, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

from common.base import Base
from models.item import Item
from models.player import Player


# ToDo Consider renaming this, should this be something like PlayerInventoryItem?
class PlayerInventory(Base):
    __tablename__ = 'player_inventory'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey(Player.id))
    item_id = Column(Integer, ForeignKey(Item.id))
    item_amount = Column(Integer)
    UniqueConstraint(player_id, item_id)
    item = relationship('models.item.Item')
