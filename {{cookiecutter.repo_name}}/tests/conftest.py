"""Module to setup Test Suite and register artifacts for tests"""

import pytest


def pytest_addoption(parser):
    """Additional options for running tests with pytest"""
    parser.addoption(
        "--slow", action="store_true", default=False, help="run slow tests"
    )


def pytest_collection_modifyitems(config, items):
    """Configure special markers on tests, so as to control execution"""
    if config.getoption("--slow"):
        # --slow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --slow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture(scope="session", autouse=True)
def run_once_on_init():
    """Things to run once for the entire test suite"""
    pass


@pytest.fixture(autouse=True)
def run_around_tests():
    """Stuff to run around every test case, like Connection initialization and Data Cleanup"""

    # Do something before running each test case

    yield

    # Do something after running each test case
