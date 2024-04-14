import os

from pyhocon import ConfigFactory


class Config(object):
    def __init__(self):
        self._config = ConfigFactory.parse_file(os.environ['CONF_PATH'])

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]