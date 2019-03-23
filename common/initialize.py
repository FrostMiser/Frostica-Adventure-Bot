from models.player import Player
from common.world import world
from configuration import settings

import json
from pathlib import Path


def initialize_player(name, player_id, session):
    player = session.query(Player).filter(Player.id == player_id).first()
    if not player:
        player = Player(id=player_id, name=name)
        session.add(player)
        player.x = settings.settings['player_starting_x']
        player.y = settings.settings['player_starting_y']
        player.health = settings.settings['player_starting_health']
        session.commit()
    return player


def initialize_world():
    if not world['tiles']:
        world_file_path = Path(__file__).resolve().parent.parent.joinpath('configuration', 'world.json')
        if world_file_path.exists():
            world_file = open(world_file_path, 'r')
            world['tiles'] = json.loads(world_file.read())
        else:
            raise Exception('World file not found. Check /configuration/world.json')
