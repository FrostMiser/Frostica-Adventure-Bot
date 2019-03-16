from sqlalchemy.orm import sessionmaker

from common.base import Base
from models.item import Item


# ToDo Add permission checking for this command
def run_command(db_engine):
    _populate_items(db_engine)
    response = 'Setup complete.'
    return response


def _populate_items(db_engine):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    session.query(Item).delete()
    session.add(Item(name='stone', forage_drop_chance=90, mine_drop_chance=120))
    session.add(Item(name='iron ore', mine_drop_chance=15))
    session.add(Item(name='gold ore', mine_drop_chance=5))
    session.add(Item(name='copper ore', mine_drop_chance=5))
    session.add(Item(name='lead ore', mine_drop_chance=5))

    session.add(Item(name='unrefined diamond', mine_drop_chance=1))
    session.add(Item(name='unrefined ruby', mine_drop_chance=2))
    session.add(Item(name='unrefined topaz', mine_drop_chance=2))
    session.add(Item(name='unrefined sapphire', mine_drop_chance=2))

    session.add(Item(name='stick', forage_drop_chance=90))
    session.add(Item(name='leaf', forage_drop_chance=20))
    session.add(Item(name='pine needle', forage_drop_chance=20))
    session.add(Item(name='brown mushroom', forage_drop_chance=5))
    session.add(Item(name='cucumber', forage_drop_chance=15, edible=True, hunger_satisfaction=5))
    session.add(Item(name='blueberry', forage_drop_chance=2, edible=True, hunger_satisfaction=2))
    session.add(Item(name='cherry', forage_drop_chance=2, edible=True, hunger_satisfaction=2))
    session.commit()
