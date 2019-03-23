from models.player import Player


def run_command(message, session):
    player = session.query(Player).filter(Player.id == message.author.id).first()
    response = '__{}__'.format(player.name)
    response += '\nHealth {}/{}'.format(player.health, player.max_health)
    response += '\nMana {}/{}'.format(player.mana, player.max_mana)
    response += '\nHunger {}/{}'.format(player.hunger, player.max_hunger)
    response += '\nThirst {}/{}'.format(player.thirst, player.max_thirst)

    if player.main_hand_item:
        response += '\n\n__Equipment__'
        response += '\nMain Hand: {}'.format(player.main_hand_item.name)

    return response
