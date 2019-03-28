from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from common.base import Base
from models.item import Item
from models.recipe import Recipe


class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredient'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey(Recipe.id))
    item_id = Column(Integer, ForeignKey(Item.id))
    item_amount = Column(Integer)
    item = relationship('models.item.Item')
