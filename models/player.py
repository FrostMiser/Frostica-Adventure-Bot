from common.base import Base

from sqlalchemy import Column, Integer, String


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    health = Column(Integer, default=100)
    mana = Column(Integer, default=0)
    max_health = Column(Integer, default=100)
    max_mana = Column(Integer, default=0)
    max_inventory_size = Column(Integer)
