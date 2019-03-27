from models.player import Player
from common.helpers import get_session


# ToDo Add mana cost and get spells from database.
def run_command(message, message_content, session):
    spell_name = ' '.join(message_content.split(" ")[1:2]) if len(message_content.split(" ")) > 1 else None

    if not spell_name:
        return 'You must say what spell you want to cast with !cast <spell>'
    if spell_name == 'convert':
        response = 'This spell is not yet supported.'
    # ToDo This version of teleport is temporary to help get around the map. Add a separate admin teleport and limit
    #      this version to a set number of tiles away from the player's location.
    elif spell_name == 'teleport':
        location_x = ' '.join(message_content.split(" ")[2:3]) if len(message_content.split(" ")) > 2 else None
        location_y = ' '.join(message_content.split(" ")[3:4]) if len(message_content.split(" ")) > 3 else None
        if location_x and location_y and location_x.isnumeric() and location_y.isnumeric() \
                and 0 <= int(location_x) < 10000 and 0 <= int(location_y) < 10000:
            player = session.query(Player).filter(Player.id == message.author.id).first()
            player.x = location_x
            player.y = location_y
            response = 'You have teleported to {} {}.'.format(location_x, location_y)
        else:
            response = 'You must say where you want to teleport to with !cast teleport x y.'
    else:
        response = 'That is not a spell you know.'
    return response
