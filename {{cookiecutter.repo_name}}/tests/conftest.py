import logging.config
import os
import pytest

from protean.globals import current_domain


def fetch_{{ cookiecutter.package_name }}_domain():
    """Fetch the core domain for running tests
    This is typically the domain to which all domain elements are registered
    """
    from {{ cookiecutter.package_name }}.domain import domain
    return domain


def configured_domain_for_session(session):
    domain = fetch_{{ cookiecutter.package_name }}_domain()

    # Construct relative path to config file
    current_path = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(current_path, "./config.py")

    if os.path.exists(config_path):
        domain.config.from_pyfile(config_path)

    if 'LOGGING_CONFIG' in domain.config:
        logging.config.dictConfig(domain.config['LOGGING_CONFIG'])

    return domain


def pytest_sessionstart(session):
    """Pytest hook to run before collecting tests.

    In this method, we fetch the domain and activate it,
    by pushing the domain_context associated with the domain.
    We can then refer to the domain everywhere else in pytest with `current_domain`
    """
    domain = configured_domain_for_session(session)
    domain.domain_context().push()


@pytest.fixture(autouse=True)
def run_around_tests():

    yield

    from protean.globals import current_domain

    for provider in current_domain.providers_list():
        provider._data_reset()
