import logging
import logging.config
import os

from protean.domain import Domain

domain = Domain("{{ cookiecutter.project_name }}")

current_path = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(current_path, "./config.py")
domain.config.from_pyfile(config_path)

logging.config.dictConfig(domain.config["LOGGING_CONFIG"])

domain.init()

# Enable Event Logging
#
# from protean.infra.event_log import EventLog, EventLogRepository
# domain.register(EventLog)
# domain.register(EventLogRepository)
