from common.helpers import get_player
from configuration import settings  # pylint: disable=no-name-in-module


# ToDo Add mana cost and get spells from database.
def run_command(message, message_content, session):
    spell_name = ' '.join(message_content.split(" ")[1:2]) if len(message_content.split(" ")) > 1 else None

    if not spell_name:
        return 'You must say what spell you want to cast with !cast <spell>'
    response = None
    player = get_player(session, message.author.id)
    if spell_name == 'convert':
        for player_inventory_item in player.inventory:
            if player_inventory_item.item.name == 'magic ore':
                if player.mana + player_inventory_item.item_amount <= player.max_mana:
                    amount = player_inventory_item.item_amount
                    player.mana = player.mana + amount
                    session.delete(player_inventory_item)
                else:
                    amount = player.mana + player_inventory_item.item_amount - player.max_mana
                    player.mana = player.mana + amount
                    player_inventory_item.item_amount = player_inventory_item.item_amount - amount

                # ToDo show how much magic ore was converted
                response = 'You convert {} magic ore into mana.'.format(amount)
        if not response:
            response = 'You do not have any magic ore to convert.'
    elif spell_name == 'heal':
        cost = 10
        if player.health >= player.max_health:
            response = 'You do not need to heal right now.'
        elif player.mana - cost < 0:
            response = 'You do not have enough mana to cast this spell.'
        else:
            player.mana = player.mana - cost
            player.health = max(player.health+10, player.max_health)
            response = 'You cast a spell and heal yourself.'
    # ToDo Do not allow teleporting outside of the map
    elif spell_name == 'teleport':
        cost = 15
        try:
            location_x = int(' '.join(message_content.split(" ")[2:3])) if len(message_content.split(" ")) > 2 else None
            location_y = int(' '.join(message_content.split(" ")[3:4])) if len(message_content.split(" ")) > 3 else None
        except ValueError:
            return 'You must say where you want to teleport to with !cast teleport distance_x distance_y.'

        if player.mana - cost < 0:
            response = 'You do not have enough mana to cast this spell.'
        elif (int(location_x) > 10 or int(location_y) > 10) and \
                message.author.id not in settings.general['admins']:  # ToDo Allow admins to teleport larger distances
            response = 'You may only teleport up to 10 tiles from your current location.'
        else:
            player.mana = player.mana - cost
            if location_x and location_y and int(location_x) < 10000 and int(location_y) < 10000:
                player.x = player.x + int(location_x)
                player.y = player.y + int(location_y)
                response = 'You have teleported to {} {}.'.format(player.x, player.y)
            else:
                response = 'You must say where you want to teleport to with !cast teleport distance_x distance_y.'
    else:
        response = 'That is not a spell you know.'
    return response
