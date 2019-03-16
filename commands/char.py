from sqlalchemy.orm import sessionmaker
from models.player import Player


def run_command(db_engine, message):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.id == message.author.id).first()
    response = '__{}__'.format(player.name)
    response += '\nHealth {}/{}'.format(player.health, player.max_health)
    response += '\nMana {}/{}'.format(player.mana, player.max_mana)

    return response
