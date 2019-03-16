from common.base import Base


def run_command(db_engine):
    Base.metadata.create_all(db_engine)
    response = 'Setup complete.'
    return response
