from enum import Enum


class EnvironmentSet(str, Enum):
    """Enum for the environment set."""

    PRODUCTION = 'production'
    DEVELOPMENT = 'development'
    STAGING = 'staging'
