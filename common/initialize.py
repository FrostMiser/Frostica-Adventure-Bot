from sqlalchemy.orm import sessionmaker
from models.player import Player


def initialize_player(db_engine, name):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.name == name).first()
    if not player:
        new_player = Player(name=name)
        session.add(new_player)
        session.commit()
