import discord
from sqlalchemy import create_engine
import settings

db_engine = create_engine(settings['database_engine'])

@client.event
async def on_message(message):
    message_content = message.content.lower()
    response = None

    if message_content.startswith('!map'):
    elif message_content.startswith('!enter'):
    elif message_content.startswith('!enter'):
    elif message_content.startswith('!move'):
    elif message_content.startswith('!cast'):
    elif message_content.startswith('!spellbook'):
    elif message_content.startswith('!forage'):
    elif message_content.startswith('!mine'):
    elif message_content.startswith('!chop'):
    elif message_content.startswith('!hunt'):
    elif message_content.startswith('!craft'):
    elif message_content.startswith('!recipes'):
    elif message_content.startswith('!use'):
    elif message_content.startswith('!char'):
    elif message_content.startswith('!inv'):
    else:
        response = 'Unknown command.'

    if response:
        await client.send_message(message.channel, response)

client.run(settings['api_token'])






