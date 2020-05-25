from sqlalchemy import Column, Integer, String, Boolean

from common.base import Base


class Tile(Base):
    __tablename__ = 'tile'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    display_emoji = Column(String)
    interactive = Column(Boolean, default=False)
    traversable = Column(Boolean, default=True)
    hunger_drain_amount = Column(Integer, default=0)
    thirst_drain_amount = Column(Integer, default=0)

    can_chop = Column(Boolean, default=False)
    can_mine = Column(Boolean, default=False)
    can_hunt = Column(Boolean, default=False)
    can_forage = Column(Boolean, default=False)
