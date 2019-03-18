from common.base import Base

from sqlalchemy import Column, Integer, String, Boolean


class RecipeIngredient(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    recipe = Column(Integer, ForeignKey(Player.id))
    item = relationship('models.item.Item')
