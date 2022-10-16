from common.enums import EnvironmentSet
from decouple import config

APPLICATION_NAME = config('APPLICATION_NAME', default='Todo List')
ENVIRONMENT: EnvironmentSet = config('ENVIRONMENT', default='development', cast=EnvironmentSet)
PYTEST_RUNNING = config('PYTEST_RUNNING', default=0, cast=int)

DATABASE_URL = ''
USE_DATABASE = config('USE_DATABASE', default=True, cast=bool)

if USE_DATABASE:
    DB_NAME = config('DB_NAME') if not PYTEST_RUNNING else 'test_db'
    DATABASE_URL = (
        f"mysql+asyncmy://{config('DB_USER')}:{config('DB_PASSWORD')}@"
        f"{config('DB_HOST')}:{config('DB_PORT')}/{DB_NAME}"
    )

SERVERS = [
    {'url': 'https://todo-list.staging.nereswe.com', 'description': 'Staging'},
    {'url': 'https://todo-list.nereswe.com', 'description': 'Production'},
]

if ENVIRONMENT == EnvironmentSet.DEVELOPMENT:
    SERVERS.insert(0, {'url': 'http://localhost:5000', 'description': 'Local'})
