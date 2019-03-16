import discord
from sqlalchemy import create_engine
import settings

import commands



db_engine = create_engine(settings['database_engine'])

@client.event
async def on_message(message):
    message_content = message.content.lower()
    response = None

    if message_content.startswith('!map'):
        response = commands.map.run_command(message, message_content)
    elif message_content.startswith('!enter'):
        response = commands.enter.run_command(message, message_content)
    elif message_content.startswith('!move'):
        response = commands.move.run_command(message, message_content)
    elif message_content.startswith('!cast'):
        response = commands.cast.run_command(message, message_content)
    elif message_content.startswith('!spellbook'):
        response = commands.spellbook.run_command(message, message_content)
    elif message_content.startswith('!forage'):
        response = commands.forage.run_command(message, message_content)
    elif message_content.startswith('!mine'):
        response = commands.mine.run_command(message, message_content)
    elif message_content.startswith('!chop'):
        response = commands.chop.run_command(message, message_content)
    elif message_content.startswith('!hunt'):
        response = commands.hunt.run_command(message, message_content)
    elif message_content.startswith('!craft'):
        response = commands.craft.run_command(message, message_content)
    elif message_content.startswith('!recipes'):
        response = commands.recipe.run_command(message, message_content)
    elif message_content.startswith('!use'):
        response = commands.use.run_command(message, message_content)
    elif message_content.startswith('!char'):
        response = commands.char.run_command(message, message_content)
    elif message_content.startswith('!inv'):
        response = commands.inv.run_command(message, message_content)
    else:
        response = 'Unknown command.'

    if response:
        await client.send_message(message.channel, response)

client.run(settings['api_token'])






