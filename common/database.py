from sqlalchemy import create_engine

from configuration import settings

db_engine = create_engine(settings.general['database_engine'])
