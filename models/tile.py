from sqlalchemy import Column, Integer, String, Boolean

from common.base import Base


class Tile(Base):
    __tablename__ = 'tile'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    display_emoji = Column(String)
    emoji_name = Column(String)
    interactive = Column(Boolean, default=False)
    traversable = Column(Boolean, default=True)
