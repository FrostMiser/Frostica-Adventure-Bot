from sqlalchemy.orm import sessionmaker

from common.base import Base
from models.item import Item


def run_command(db_engine):
    _populate_items(db_engine)
    response = 'Setup complete.'
    return response


def _populate_items(db_engine):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    session.add(Item(name='Stone Ore', forage_drop_chance=90, mine_drop_chance=120))
    session.add(Item(name='Iron Ore', mine_drop_chance=15))
    session.add(Item(name='Gold Ore', mine_drop_chance=5))
    session.add(Item(name='Copper Ore', mine_drop_chance=5))
    session.add(Item(name='Lead Ore', mine_drop_chance=5))

    session.add(Item(name='Unrefined Diamond', mine_drop_chance=1))
    session.add(Item(name='Unrefined Ruby', mine_drop_chance=2))
    session.add(Item(name='Unrefined Topaz', mine_drop_chance=2))
    session.add(Item(name='Unrefined Sapphire', mine_drop_chance=2))

    session.add(Item(name='Stick', forage_drop_chance=90))
    session.add(Item(name='Leaf', forage_drop_chance=20))
    session.add(Item(name='Pine Needle', forage_drop_chance=20))
    session.add(Item(name='Brown Mushroom', forage_drop_chance=5))
    session.add(Item(name='Cucumber', forage_drop_chance=5, edible=True, hunger_satisfaction=5))
    session.add(Item(name='Blueberry', forage_drop_chance=2, edible=True, hunger_satisfaction=2))
    session.add(Item(name='Cherry', forage_drop_chance=2, edible=True, hunger_satisfaction=2))
    session.commit()
