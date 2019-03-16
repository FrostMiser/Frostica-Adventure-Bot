from common.base import Base


def run_command(db_engine):
    response = 'This command is not yet supported.'
    Base.metadata.create_all(db_engine)
    return response
