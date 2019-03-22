from models.player import Player
from common.helpers import get_session


# ToDo Add mana cost and get spells from database. This version of teleport is temporary to help get around the map
def run_command(message, message_content):
    spell_name = ' '.join(message_content.split(" ")[1:2]) if len(message_content.split(" ")) > 1 else None

    if not spell_name:
        return 'You must say what spell you want to case with !cast <spell>'
    if spell_name == 'teleport':
        location_x = ' '.join(message_content.split(" ")[2:3]) if len(message_content.split(" ")) > 2 else None
        location_y = ' '.join(message_content.split(" ")[3:4]) if len(message_content.split(" ")) > 3 else None
        if location_x and location_y and location_x.isnumeric() and location_y.isnumeric() \
                    and 0 < int(location_x) < 1000 and 0 < int(location_y) < 1000:
            session = get_session()
            player = session.query(Player).filter(Player.id == message.author.id).first()
            player.x = location_x
            player.y = location_y
            session.commit()
            response = 'You have teleported to {} {}.'.format(location_x, location_y)
        else:
            response = 'You must say where you want to teleport to with !cast teleport x y.'
    else:
        response = 'That is not a spell you know.'
    return response
