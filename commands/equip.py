from common.helpers import get_session, get_item_by_name
from models.player import Player
from models.player_inventory import PlayerInventory


def run_command(message, message_content, session):
    item_name = ' '.join(message_content.split(" ")[1:]) if len(message_content.split(" ")) > 1 else None
    if not item_name:
        return 'You must say which item you want to equip with !equip <item>.'

    player = session.query(Player).filter(Player.id == message.author.id).first()
    item_lookup = get_item_by_name(item_name, session)
    if not item_lookup:
        return 'That item does not exist.'

    player_inventory_item = session.query(PlayerInventory).filter(
        PlayerInventory.player_id == message.author.id, PlayerInventory.item_id == item_lookup.id).first()
    if player_inventory_item:
        if player_inventory_item.item.equipable:
            # Add currently equipped item back into the players inventory
            if player.main_hand_item:
                player_inventory_item_add_back = session.query(PlayerInventory).filter(
                    PlayerInventory.player_id == message.author.id,
                    PlayerInventory.item_id == player.main_hand_item.id).first()
                if player_inventory_item_add_back:
                    player_inventory_item_add_back.item_amount += 1
                else:
                    session.add(PlayerInventory(player_id=player.id, item_amount=1, item=player.main_hand_item))
            player.main_hand_item = player_inventory_item.item
            if player_inventory_item.item_amount > 1:
                player_inventory_item.item_amount -= 1
            else:
                session.delete(player_inventory_item)
            response = 'You equip your {}.'.format(item_name)
        else:
            response = 'That item may not be equipped.'
    else:
        response = 'You do not own that item.'
    return response
