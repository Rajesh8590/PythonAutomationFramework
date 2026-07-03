from configparser import ConfigParser
from pathlib import Path


class ConfigReader:

    @staticmethod
    def get_config():
        config = ConfigParser()
        config_path = (Path(__file__).parent.parent / "config.ini")
        config.read(config_path)
        return config["DEFAULT"]