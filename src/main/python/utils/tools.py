import os

import loguru
from pyhocon import ConfigFactory
from loguru import logger


class Config(object):
    def __init__(self):
        self._config = ConfigFactory.parse_file(os.environ['CONF_PATH'])

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]


def custom_logger(path: str, level: str = "INFO") -> loguru.logger:
    """
    A logger (from loguru) used to give some information to the user during the computation
    in order to monitor the app
    :param path: The log path folder
    :param level: The log level which will be written in the log file
    :return: A configured loguru logger that can be used and which will write in log file
    """
    logger.add(
        sink="{}/ml.log".format(path),
        level=level,
        colorize=True,
        rotation="1 week",
        format="{time} {level} {message}"
    )
    return logger
