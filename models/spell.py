from sqlalchemy import Column, Integer, String

from common.base import Base


class Player(Base):
    __tablename__ = 'spell'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    mana_cost = Column(Integer)
