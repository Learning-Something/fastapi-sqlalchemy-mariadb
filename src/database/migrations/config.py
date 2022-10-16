from alembic.config import Config
from settings import DATABASE_URL

alembic_cfg = Config()
alembic_cfg.set_main_option("script_location", "src/database/migrations")
alembic_cfg.set_main_option("sqlalchemy.url", DATABASE_URL)
