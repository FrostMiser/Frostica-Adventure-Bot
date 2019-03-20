from sqlalchemy import Column, Integer, String

from common.base import Base
from models.player import Player
from models.spell import Spell


class PlayerSpellbook(Base):
    __tablename__ = 'player_spellbook'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey(Player.id))
    spell_id = Column(Integer, ForeignKey(Spell.id))
