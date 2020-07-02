# cSpell: disable

import datetime
import os

from protean.utils import Database, IdentityStrategy


DEBUG = True

# Parse domain directory and autoload domain modules
AUTOLOAD_DOMAIN = True

# A secret key for this particular Protean installation. Used in secret-key
# hashing algorithms.
SECRET_KEY = "1$jp0neQpaU8issDzX4uQ*eEfDEh$TOOKd$fFJBRyDQNvUl25y"

# Flag indicates that we are testing
TESTING = True

# Database Configuration
DATABASES = {
    "default": {"PROVIDER": "protean.impl.repository.dict_repo.DictProvider"},
    "sqlite": {
        "PROVIDER": "protean.impl.repository.sqlalchemy_repo.SAProvider",
        "DATABASE": Database.SQLITE.value,
        "DATABASE_URI": "sqlite:///test.db",
    },
    "postgres": {
        "PROVIDER": "protean.impl.repository.sqlalchemy_repo.SAProvider",
        "DATABASE": Database.POSTGRESQL.value,
        "DATABASE_URI": os.getenv(
            "POSTGRESQL_DATABASE_URI",
            "postgresql://{{ cookiecutter.package_name }}:pwd@localhost:5432/{{ cookiecutter.package_name }}_dev",
        ),
    },
}

# Identity strategy to use when persisting Entities/Aggregates.
#
# Options:
#
#   * IdentityStrategy.UUID: Default option, and preferred. Identity is a UUID and generated during `build` time.
#       Persisted along with other details into the data store.
#   * IdentityStrategy.DATABASE: Let the database generate unique identity during persistence
#   * IdentityStrategy.FUNCTION: Special function that returns a unique identifier
IDENTITY_STRATEGY = IdentityStrategy.UUID

# Messaging Mediums
BROKERS = {
    "default": {"PROVIDER": "protean.impl.broker.memory_broker.MemoryBroker",},
    "celery": {
        "PROVIDER": "protean.impl.broker.celery_broker.CeleryBroker",
        "URI": os.environ.get("BROKER_URI") or "redis://127.0.0.1:6379/2",
        "IS_ASYNC": True,
    },
}

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",},
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
    },
    "loggers": {
        "protean": {"handlers": ["console"], "level": "INFO",},
        "protean.impl.broker.celery": {"handlers": ["console"], "level": "INFO",},
        "{{ cookiecutter.package_name }}": {"handlers": ["console"], "level": "INFO",},
    },
}
