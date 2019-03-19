from sqlalchemy.orm import sessionmaker
from models.player import Player 

def run_command(db_engine, message, message_content): 
  session_maker = sessionmaker(bind=db_engine) 
  session = session_maker() 
  player = session.query(Player).filter(Player.id == message.author.id).first() 

  direction = ''.join(message_content.split(" ")[1:]) if len(message_content.split(" ")) > 1 else None
  response = ""
  
  if direction == 'north': 
    player.y += 1
    response += "you move north.\n"
  elif direction == 'south': 
    player.y -= 1
    response += "you move south.\n"
  elif direction == 'east': 
    player.x += 1
    response += "you move east.\n"
  elif direction == 'west': 
    player.x -= 1
    response += "you move west.\n"
  else: 
    response = ("You must say which direction you want to use with !use <direction>.\n"
                "valid directions are north, east, south, and west.")
    return response

  session.commit()
  response += " " + f"your position is now at [{player.x}, {player.y}]."
  return response