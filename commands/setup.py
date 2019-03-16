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
    session.add(Item(name='copper ore', mine_drop_chance=10))
    session.add(Item(name='lead ore', mine_drop_chance=10))
    session.add(Item(name='nickel ore', mine_drop_chance=7))
    session.add(Item(name='tin ore', mine_drop_chance=8))
    session.add(Item(name='silver ore', mine_drop_chance=3))
    session.add(Item(name='platinum ore', mine_drop_chance=1))
    session.add(Item(name='zinc ore', mine_drop_chance=7))

    session.add(Item(name='unrefined diamond', mine_drop_chance=1))
    session.add(Item(name='unrefined ruby', mine_drop_chance=2))
    session.add(Item(name='unrefined topaz', mine_drop_chance=2))
    session.add(Item(name='unrefined sapphire', mine_drop_chance=2))
    session.add(Item(name='unrefined jade', mine_drop_chance=2))
    session.add(Item(name='unrefined amber', mine_drop_chance=2))
    session.add(Item(name='unrefined lapis lazuli', mine_drop_chance=2))
    session.add(Item(name='unrefined turquoise', mine_drop_chance=2))
    session.add(Item(name='unrefined amethyst', mine_drop_chance=2))
    session.add(Item(name='unrefined emerald', mine_drop_chance=2))
    session.add(Item(name='unrefined opal', mine_drop_chance=2))
    session.add(Item(name='unrefined quartz', mine_drop_chance=2))
    session.add(Item(name='unrefined peridot', mine_drop_chance=2))
    session.add(Item(name='unrefined onyx', mine_drop_chance=2))

    session.add(Item(name='stick', forage_drop_chance=90))
    session.add(Item(name='leaf', forage_drop_chance=20))
    session.add(Item(name='pine needle', forage_drop_chance=20))
    session.add(Item(name='brown mushroom', forage_drop_chance=5))
    session.add(Item(name='cucumber', forage_drop_chance=10, edible=True, hunger_satisfaction=5))
    session.add(Item(name='blueberry', forage_drop_chance=10, edible=True, hunger_satisfaction=1))
    session.add(Item(name='cherry', forage_drop_chance=10, edible=True, hunger_satisfaction=1))
    session.add(Item(name='banana', forage_drop_chance=10, edible=True, hunger_satisfaction=2))
    session.add(Item(name='orange', forage_drop_chance=10, edible=True, hunger_satisfaction=2))
    session.add(Item(name='pear', forage_drop_chance=10, edible=True, hunger_satisfaction=2))
    session.add(Item(name='carrot', forage_drop_chance=10, edible=True, hunger_satisfaction=2))
    session.commit()
