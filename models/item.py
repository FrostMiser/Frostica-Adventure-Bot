from common.base import Base

from sqlalchemy import Column, Integer, String, Boolean


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    forage_drop_chance = Column(Integer, default=0)
    mine_drop_chance = Column(Integer, default=0)
    chop_drop_chance = Column(Integer, default=0)
    hunt_drop_chance = Column(Integer, default=0)
    edible = Column(Boolean, default=False)
    hunger_satisfaction = Column(Integer, default=0)
