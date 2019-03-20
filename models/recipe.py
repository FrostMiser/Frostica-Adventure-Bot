from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from common.base import Base
from models.item import Item


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    ingredients = relationship('models.recipe_ingredient.RecipeIngredient')
    item_id = Column(Integer, ForeignKey(Item.id))
    item = relationship('models.item.Item')
