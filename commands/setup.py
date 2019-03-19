from sqlalchemy.orm import sessionmaker

from common.base import Base
from common.helpers import get_item
from models.item import Item
from models.recipe import Recipe
from models.recipe_ingredient import RecipeIngredient
from common.database import db_engine

# ToDo Add permission checking for this command
def run_command():
    _populate_items(db_engine)
    _populate_recipes(db_engine)
    response = 'Setup complete.'
    return response


def _populate_items(db_engine):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    session.query(Item).delete()

    # 1 - 200 mined items
    session.add(Item(id=1, name='stone', forage_drop_chance=90, mine_drop_chance=120))
    session.add(Item(id=2, name='iron ore', mine_drop_chance=15))
    session.add(Item(id=3, name='gold ore', mine_drop_chance=5))
    session.add(Item(id=4, name='copper ore', mine_drop_chance=10))
    session.add(Item(id=5, name='lead ore', mine_drop_chance=10))
    session.add(Item(id=6, name='nickel ore', mine_drop_chance=7))
    session.add(Item(id=7, name='tin ore', mine_drop_chance=8))
    session.add(Item(id=8, name='silver ore', mine_drop_chance=3))
    session.add(Item(id=9, name='platinum ore', mine_drop_chance=1))
    session.add(Item(id=10, name='zinc ore', mine_drop_chance=7))

    session.add(Item(id=11, name='unrefined diamond', mine_drop_chance=1))
    session.add(Item(id=12, name='unrefined ruby', mine_drop_chance=2))
    session.add(Item(id=13, name='unrefined topaz', mine_drop_chance=2))
    session.add(Item(id=14, name='unrefined sapphire', mine_drop_chance=2))
    session.add(Item(id=15, name='unrefined jade', mine_drop_chance=2))
    session.add(Item(id=16, name='unrefined amber', mine_drop_chance=2))
    session.add(Item(id=17, name='unrefined lapis lazuli', mine_drop_chance=2))
    session.add(Item(id=18, name='unrefined turquoise', mine_drop_chance=2))
    session.add(Item(id=19, name='unrefined amethyst', mine_drop_chance=2))
    session.add(Item(id=20, name='unrefined emerald', mine_drop_chance=2))
    session.add(Item(id=21, name='unrefined opal', mine_drop_chance=2))
    session.add(Item(id=22, name='unrefined quartz', mine_drop_chance=2))
    session.add(Item(id=23, name='unrefined peridot', mine_drop_chance=2))
    session.add(Item(id=24, name='unrefined onyx', mine_drop_chance=2))

    # 201 - 400 foraged items
    session.add(Item(id=201, name='stick', forage_drop_chance=120))
    session.add(Item(id=202, name='leaf', forage_drop_chance=20))
    session.add(Item(id=203, name='pine needle', forage_drop_chance=20))
    session.add(Item(id=204, name='brown mushroom', forage_drop_chance=5))
    session.add(Item(id=205, name='cucumber', forage_drop_chance=10, edible=True, hunger_satisfaction=5))
    session.add(Item(id=206, name='blueberry', forage_drop_chance=10, edible=True, hunger_satisfaction=1))
    session.add(Item(id=207, name='cherry', forage_drop_chance=10, edible=True, hunger_satisfaction=1))
    session.add(Item(id=208, name='banana', forage_drop_chance=10, edible=True, hunger_satisfaction=2))
    session.add(Item(id=209, name='orange', forage_drop_chance=10, edible=True, hunger_satisfaction=2))
    session.add(Item(id=210, name='pear', forage_drop_chance=10, edible=True, hunger_satisfaction=2))
    session.add(Item(id=211, name='carrot', forage_drop_chance=10, edible=True, hunger_satisfaction=2))
    session.add(Item(id=212, name='broccoli', forage_drop_chance=5, edible=True, hunger_satisfaction=7))
    session.add(Item(id=213, name='spinach', forage_drop_chance=2, edible=True, hunger_satisfaction=1))
    session.add(Item(id=214, name='cauliflower', forage_drop_chance=1, edible=True, hunger_satisfaction=9))
    session.add(Item(id=215, name='radish', forage_drop_chance=1, edible=True, hunger_satisfaction=9))
    # 401 - 600 hunting items
    # 601 - 800 wood chopping items

    # 801 - 1200 crafted items, tools, armor, etc
    session.add(Item(id=401, name='basic pickaxe'))
    session.add(Item(id=402, name='basic axe'))
    session.commit()


def _populate_recipes(db_engine):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    session.query(Recipe).delete()
    session.query(RecipeIngredient).delete()

    # Basic Pickaxe
    basic_pickaxe = Recipe(id=1, name='basic pickaxe', item=get_item('basic pickaxe'))
    session.add(basic_pickaxe)

    basic_pickaxe_ingredient_1 = RecipeIngredient(recipe_id=basic_pickaxe.id, item=get_item('stone'), item_amount=7)
    session.add(basic_pickaxe_ingredient_1)
    basic_pickaxe_ingredient_2 = RecipeIngredient(recipe_id=basic_pickaxe.id, item=get_item('stick'), item_amount=4)
    session.add(basic_pickaxe_ingredient_2)

    # Basic axe
    basic_pickaxe = Recipe(id=1, name='basic axe', item=get_item('basic axe'))
    session.add(basic_pickaxe)

    basic_pickaxe_ingredient_1 = RecipeIngredient(recipe_id=basic_pickaxe.id, item=get_item('stone'), item_amount=5)
    session.add(basic_pickaxe_ingredient_1)
    basic_pickaxe_ingredient_2 = RecipeIngredient(recipe_id=basic_pickaxe.id, item=get_item('stick'), item_amount=4)
    session.add(basic_pickaxe_ingredient_2)

    session.commit()
    return
