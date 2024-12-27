import logging.config
from os import path


log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(log_file_path)

pytest_plugins = [
    "src.fixtures.system.browser"
]


def pytest_addoption(parser):
    parser.addini("path_to_driver_chrome", "Selenium driver chrome")
