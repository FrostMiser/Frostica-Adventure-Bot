from sqlalchemy.orm import sessionmaker

from common.database import db_engine
from models.player import Player


def run_command(message):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.id == message.author.id).first()
    response = '__{}__'.format(player.name)
    response += '\nHealth {}/{}'.format(player.health, player.max_health)
    response += '\nMana {}/{}'.format(player.mana, player.max_mana)
    response += '\nHunger {}/{}'.format(player.hunger, player.max_hunger)
    response += '\nThirst {}/{}'.format(player.thirst, player.max_thirst)
    # ToDo Display equipment being worn

    return response
