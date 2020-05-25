def run_command():
    commands = {
        '!cast': 'Cast a spell, use !cast <spell>.',
        '!char': 'Character information.',
        '!chop': 'Chop nearby trees.',
        '!craft <item>': 'Craft an item, use !craft <item>.',
        '!equip <item>': 'Equip an item, use !equip <item>.',
        '!forage': 'Forage for items nearby.',
        '!help': 'Show this help screen.',
        '!hunt': 'Hunt in the nearby area.',
        '!inv': 'Show your inventory.',
        '!map': 'Show the nearby map.',
        '!mine': 'Mine in the nearby area.',
        '!move': 'Move to a different area, use !move <n|s|e|w>.',
        '!recipes': 'View recipes, or view recipe ingredients with !recipes <recipe>.',
        '!use': 'Use an item with !use <item>. Used to eat, drink and equip items.',
        '!spellbook': 'View your book of spells.',
    }

    response = '__List of commands__'
    for command, description in commands.items():
        response += '\n**{}**: `{}`'.format(command, description)

    return response
