import discord
from sqlalchemy import create_engine
import settings


from commands import cast, char, chop, craft, enter, forage, hunt, inv, map, move, recipes, spellbook, use


db_engine = create_engine(settings.settings['database_engine'])
client = discord.Client()

@client.event
async def on_message(message):
    message_content = message.content.lower()
    command =  message_content.split(" ")[0] if message_content.split(" ") else None
    if not command or message.author == client.user: return

    if command == '!map':
        response = map.run_command(message, message_content)
    elif command == '!enter':
        response = commands.enter.run_command(message, message_content)
    elif command == '!move':
        response = commands.move.run_command(message, message_content)
    elif command == '!cast':
        response = commands.cast.run_command(message, message_content)
    elif command == '!spellbook':
        response = commands.spellbook.run_command(message, message_content)
    elif command == '!forage':
        response = commands.forage.run_command(message, message_content)
    elif command == '!mine':
        response = commands.mine.run_command(message, message_content)
    elif command == '!chop':
        response = commands.chop.run_command(message, message_content)
    elif command == '!hunt':
        response = commands.hunt.run_command(message, message_content)
    elif command == '!craft':
        response = commands.craft.run_command(message, message_content)
    elif command == '!recipes':
        response = commands.recipe.run_command(message, message_content)
    elif command == '!use':
        response = commands.use.run_command(message, message_content)
    elif command == '!char':
        response = commands.char.run_command(message, message_content)
    elif command == '!inv':
        response = commands.inv.run_command(message, message_content)
    else:
        response = 'Unknown command.'

    if response:
        await client.send_message(message.channel, response)

client.run(settings.settings['api_token'])






