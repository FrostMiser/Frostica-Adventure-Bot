from sqlalchemy import create_engine

from configuration import settings

db_engine = create_engine(settings.settings['database_engine'])
