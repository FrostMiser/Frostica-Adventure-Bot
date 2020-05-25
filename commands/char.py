from common.helpers import get_player


def run_command(player_id, session):
    player = get_player(session, player_id)
    response = '__{}__'.format(player.name)
    response += '\n:heart: Health: {}%'.format(round((player.health/player.max_health)*100))
    if player.max_mana > 0:
        response += '\n:sparkles: Mana: {}%'.format(round((player.mana/player.max_mana)*100))
    response += '\n:cake: Hunger: {}%'.format(round((player.hunger/player.max_hunger)*100))
    response += '\n:droplet: Thirst: {}%'.format(round((player.thirst/player.max_thirst)*100))

    if player.main_hand_item:
        response += '\n\n__Equipment__'
        response += '\nMain Hand: {}'.format(player.main_hand_item.name)

    return response
