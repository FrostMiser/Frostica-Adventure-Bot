from configuration import settings  # pylint: disable=no-name-in-module


def run_command(message):
    if message.author.id not in settings.general['admins']:
        response = 'You must be an admin to use this command.'
    else:
        response = 'This command is not yet supported.'
    return response
