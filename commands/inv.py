from sqlalchemy.orm import sessionmaker
from models.player import Player


def run_command(db_engine, message):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player_inventory = session.query(Player).filter(Player.id == message.author.id).all()
    response = '__{}__'.format(player.name)
    response += '\nHealth {}/{}'.format(player.health, player.max_health)
    response += '\nMana {}/{}'.format(player.mana, player.max_mana)

    return response
