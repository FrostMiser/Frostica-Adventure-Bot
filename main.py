import discord
import settings

from sqlalchemy import create_engine

from commands import cast, char, chop, craft, enter, forage, hunt, inv, map, mine, move, recipes, spellbook, use, setup, clear_database
from common.initialize import initialize_player
from common.base import Base

db_engine = create_engine(settings.settings['database_engine'])
client = discord.Client()
Base.metadata.create_all(db_engine)

@client.event
async def on_message(message):
    message_content = message.content.lower()
    command =  message_content.split(" ")[0] if message_content.split(" ") else None
    if not command or message.author == client.user: return
    initialize_player(db_engine, message.author.name, message.author.id)

    if command == '!map':
        response = map.run_command(message, message_content)
    elif command == '!enter':
        response = enter.run_command(message, message_content)
    elif command == '!move':
        response = move.run_command(message, message_content)
    elif command == '!cast':
        response = cast.run_command(message, message_content)
    elif command == '!spellbook':
        response = spellbook.run_command(message, message_content)
    elif command == '!forage':
        response = forage.run_command(message, db_engine)
    elif command == '!mine':
        response = mine.run_command(message, message_content)
    elif command == '!chop':
        response = chop.run_command(message, message_content)
    elif command == '!hunt':
        response = hunt.run_command(message, message_content)
    elif command == '!craft':
        response = craft.run_command(message, message_content)
    elif command == '!recipes':
        response = recipe.run_command(message, message_content)
    elif command == '!use':
        response = use.run_command(message, message_content)
    elif command == '!char':
        response = char.run_command(db_engine, message)
    elif command == '!inv':
        response = inv.run_command(db_engine, message)
    elif command == '!setup':
        response = setup.run_command(db_engine)
    elif command == '!clear_database':
        response = clear_database.run_command(db_engine)
    else:
        response = 'Unknown command.'

    if response:
        await client.send_message(message.channel, response)

client.run(settings.settings['api_token'])






