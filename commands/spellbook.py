

def run_command():
    response = '__Book of Spells__'
    spells = {
        'convert': 'Convert magic ore into mana.',
        'teleport': 'Teleport up to 10 tiles away.',
    }

    response = '__Spell Book__'
    for command, description in spells.items():
        response += '\n**{}**: `{}`'.format(command, description)

    return response
