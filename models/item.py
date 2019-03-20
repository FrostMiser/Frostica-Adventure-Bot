from sqlalchemy import Column, Integer, String, Boolean

from common.base import Base


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

    equipable = Column(Boolean, default=False)
    can_mine = Column(Boolean, default=False)
    can_chop = Column(Boolean, default=False)
    can_hunt = Column(Boolean, default=False)
