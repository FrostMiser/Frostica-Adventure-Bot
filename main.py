"""This is the main module which runs this application"""
from commands import cast, char, chop, craft, enter, forage, hunt, inv, map as area_map, mine, move, recipes, spellbook,\
    use, setup
import discord

import settings
from common.initialize import initialize_player
from common.base import Base
from common.database import db_engine


client = discord.Client()
Base.metadata.create_all(db_engine)


@client.event
async def on_message(message):
    """Main chat message event"""
    message_content = message.content.lower()
    command = message_content.split(" ")[0] if message_content.split(" ") else None
    if not command or message.author == client.user:
        return

    if not command.startswith('!'):
        return

    initialize_player(message.author.name, message.author.id)
    
    if command == '!map':
        response = area_map.run_command(message, message_content)
    elif command == '!enter':
        response = enter.run_command(message, message_content)
    elif command == '!move':
        response = move.run_command(db_engine, message, message_content)
    elif command == '!cast':
        response = cast.run_command(message, message_content)
    elif command == '!spellbook':
        response = spellbook.run_command(message, message_content)
    elif command == '!forage':
        response = forage.run_command(message)
    elif command == '!mine':
        response = mine.run_command(message)
    elif command == '!chop':
        response = chop.run_command(message, message_content)
    elif command == '!hunt':
        response = hunt.run_command(message, message_content)
    elif command == '!craft':
        response = craft.run_command(message, message_content)
    elif command == '!recipes':
        response = recipes.run_command(message, message_content)
    elif command == '!use':
        response = use.run_command(message, message_content)
    elif command == '!char':
        response = char.run_command(message)
    elif command == '!inv':
        response = inv.run_command(message)
    elif command == '!setup':
        response = setup.run_command()
    else:
        response = "Unknown command."

    if response:
        await client.send_message(message.channel, response)

client.run(settings.settings['api_token'])
