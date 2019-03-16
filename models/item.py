from common.base import Base

from sqlalchemy import Column, Integer, String


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    forage_drop_chance = Column(Integer, default=0)
    mine_drop_chance = Column(Integer, default=0)
    hunt_drop_chance = Column(Integer, default=0)
