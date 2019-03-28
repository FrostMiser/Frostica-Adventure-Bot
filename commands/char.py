from models.player import Player


def run_command(message, session):
    player = session.query(Player).filter(Player.id == message.author.id).first()
    response = '__{}__'.format(player.name)
    response += '\nHealth {}%'.format((player.health/player.max_health)*100)
    if player.max_mana > 0:
        response += '\nMana {}%'.format((player.mana/player.max_mana)*100)
    response += '\nHunger {}%'.format((player.hunger/player.max_hunger)*100)
    response += '\nThirst {}%'.format((player.thirst/player.max_thirst)*100)

    if player.main_hand_item:
        response += '\n\n__Equipment__'
        response += '\nMain Hand: {}'.format(player.main_hand_item.name)

    return response
