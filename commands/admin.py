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
        elif subcommand == 'setlocation':
            try:
                location_x = int(' '.join(message_content.split(" ")[2:3])) if len(
                    message_content.split(" ")) > 2 else None
                location_y = int(' '.join(message_content.split(" ")[3:4])) if len(
                    message_content.split(" ")) > 3 else None
            except ValueError:
                return 'You must say which location, !admin setlocation x y.'
            player.x = location_x
            player.y = location_y
            response = f"Your location has been set to: {location_x}, {location_y}"
        elif subcommand == 'feed':
            player.hunger = player.max_hunger
            player.thirst = player.max_thirst
            response = 'Your hunger and thirst have been filled.'
        else:
            response = 'Unknown command. Available admin commands are: maxmana, maxhealth, feed.'
    return response
