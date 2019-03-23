from models.player import Player


def initialize_player(name, player_id, session):
    player = session.query(Player).filter(Player.id == player_id).first()
    if not player:
        new_player = Player(id=player_id, name=name)
        session.add(new_player)
        session.commit()
    return player
