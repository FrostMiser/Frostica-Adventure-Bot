from sqlalchemy import create_engine

import settings

db_engine = create_engine(settings.settings['database_engine'])
