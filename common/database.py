"""This is the global database engine"""
from sqlalchemy import create_engine

from configuration import settings  # pylint: disable=import-error

db_engine = create_engine(settings.general['database_engine'])
