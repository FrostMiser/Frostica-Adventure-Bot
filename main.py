"""This is the main module which runs this application"""
from commands import cast, char, chop, craft, enter, forage, hunt, inv, map as area_map, mine, move, recipes, spellbook, \
    use, setup, equip, help as command_help
import discord

from configuration import settings
from common.base import Base
from common.database import db_engine
from common.initialize import initialize_player, initialize_world
from common.helpers import get_session, complete_command

client = discord.Client()
Base.metadata.create_all(db_engine)


@client.event
async def on_message(message):
    """Main chat message event"""
    session = get_session()

    message_content = message.content.lower()
    command = message_content.split(" ")[0] if message_content.split(" ") else None
    if not command or message.author == client.user:
        return

    if not command.startswith('!'):
        return

    player = initialize_player(message.author.name, message.author.id, session)
    initialize_world()

    if command == '!map':
        response = area_map.run_command(message, session)
    elif command == '!enter':
        response = enter.run_command()
    elif command == '!move':
        response = move.run_command(message, message_content, session)
    elif command in ['!cast', '!c']:
        response = cast.run_command(message, message_content, session)
    elif command == '!spellbook':
        response = spellbook.run_command()
    elif command == '!forage':
        response = forage.run_command(message, session)
    elif command == '!mine':
        response = mine.run_command(message, session)
    elif command == '!chop':
        response = chop.run_command(message, session)
    elif command == '!hunt':
        response = hunt.run_command(message, session)
    elif command == '!craft':
        response = craft.run_command(message, message_content)
    elif command == '!recipes':
        response = recipes.run_command(message_content, session)
    elif command == '!use':
        response = use.run_command(message, message_content, session)
    elif command == '!char':
        response = char.run_command(message, session)
    elif command == '!inv':
        response = inv.run_command(message, session)
    elif command == '!setup':
        response = setup.run_command(message, session)
    elif command == '!equip':
        response = equip.run_command(message, message_content, session)
    elif command == '!help':
        response = command_help.run_command()
    else:
        response = "Unknown command."

    response += complete_command(player, session)
    session.commit()

    if response:
        await client.send_message(message.channel, response)

client.run(settings.general['api_token'])
