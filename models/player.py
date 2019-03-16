from sqlalchemy import Column, Integer, String


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    health = Column(Integer)
    mana = Column(Integer)
    max_inventory_size = Column(Integer)
