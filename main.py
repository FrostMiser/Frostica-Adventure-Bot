import discord
import sqlite3


@client.event
async def on_message(message):
    message_content = message.content.lower()
    response = None

    if content.startswith('!map'):
    elif content.startswith('!enter'):
    elif content.startswith('!enter'):
    elif content.startswith('!move'):
    elif content.startswith('!cast'):
    elif content.startswith('!spellbook'):
    elif content.startswith('!forage'):
    elif content.startswith('!mine'):
    elif content.startswith('!chop'):
    elif content.startswith('!hunt'):
    elif content.startswith('!craft'):
    elif content.startswith('!recipes'):
    elif content.startswith('!use'):
    elif content.startswith('!char'):
    elif content.startswith('!inv'):
    else:
        response = 'Unknown command.'

    if response:
        await client.send_message(message.channel, response)

client.run(settings.TOKEN)






