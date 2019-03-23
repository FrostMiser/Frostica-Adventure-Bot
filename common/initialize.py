from models.player import Player


def initialize_player(name, player_id, session):
    player = session.query(Player).filter(Player.id == player_id).first()
    if not player:
        player = Player(id=player_id, name=name)
        session.add(player)
        session.commit()
    return player
