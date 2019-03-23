from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from common.base import Base
from models.item import Item

class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    x = Column(Integer, default=0)
    y = Column(Integer, default=0)
    name = Column(String)
    health = Column(Integer, default=10)
    hunger = Column(Integer, default=100)
    max_hunger = Column(Integer, default=100)
    thirst = Column(Integer, default=100)
    max_thirst = Column(Integer, default=100)
    mana = Column(Integer, default=0)
    max_health = Column(Integer, default=100)
    max_mana = Column(Integer, default=0)
    max_inventory_size = Column(Integer)
    inventory = relationship('models.player_inventory.PlayerInventory')
    dimension = Column(String, default='overworld')

    main_hand_item_id = Column(Integer, ForeignKey(Item.id))
    main_hand_item = relationship('models.item.Item', foreign_keys=[main_hand_item_id])
