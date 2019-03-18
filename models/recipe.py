from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from common.base import Base


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    ingredients = relationship('models.recipe_ingredient.RecipeIngredient')
