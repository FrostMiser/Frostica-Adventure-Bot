from configuration import settings  # pylint: disable=no-name-in-module
from common.helpers import get_player


def run_command(message, message_content, session):
    subcommand = ' '.join(message_content.split(" ")[1:2]) if len(message_content.split(" ")) > 1 else None
    player = get_player(session, message.author.id)

    if message.author.id not in settings.general['admins']:
        response = 'You must be an admin to use this command.'
    else:
        if subcommand == 'maxmana':
            player.mana = player.max_mana
            response = 'Your mana has been set to your max mana.'
        elif subcommand == 'maxhealth':
            player.health = player.max_health
            response = 'Your health has been set to your max health.'
        elif subcommand == 'feed':
            player.health = player.hunger
            response = 'Your health has been set to your max health.'
        else:
            response = 'Unknown command. Available admin commands are: maxmana, maxhealth, feed.'
    return response
