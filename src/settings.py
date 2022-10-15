from common.enums import EnvironmentSet
from decouple import config

APPLICATION_NAME = config('APPLICATION_NAME', default='Todo List')
ENVIRONMENT: EnvironmentSet = config('ENVIRONMENT', default='development', cast=EnvironmentSet)

DATABASE_URL = ''
USE_DATABASE = config('USE_DATABASE', default=True, cast=bool)

if USE_DATABASE:
    DATABASE_URL = (
        f"mysql+asyncmy://{config('DB_USER')}:{config('DB_PASSWORD')}@"
        f"{config('DB_HOST')}/{config('DB_NAME')}"
    )

SERVERS = [
    {'url': 'https://todo-list.staging.nereswe.com', 'description': 'Staging'},
    {'url': 'https://todo-list.nereswe.com', 'description': 'Production'},
]

if ENVIRONMENT == EnvironmentSet.DEVELOPMENT:
    SERVERS.insert(0, {'url': 'http://localhost:5000', 'description': 'Local'})
