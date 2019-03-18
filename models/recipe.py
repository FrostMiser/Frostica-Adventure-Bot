from common.base import Base

from sqlalchemy import Column, Integer, String, Boolean


class Recipe(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    ingredients = relationship('models.recipe_ingredient.RecipeIngredient', )