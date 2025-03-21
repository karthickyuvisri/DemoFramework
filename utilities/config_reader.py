import configparser
import os.path


class ConfigReader:
    __BASE_FILE_PATH = "C:\\Users\\karth\\PycharmProjects\\DemoE2EFramework\\configurations"

    def __init__(self, filename="base_config.ini"):
        self.configreader = configparser.RawConfigParser()
        self.configreader.read(os.path.join(self.__BASE_FILE_PATH, filename))

    def get_base_url(self):
        return self.configreader.get("common", "baseurl")

    def get_login_creds(self):
        return [self.configreader.get("login", "username"), self.configreader.get("login", "password")]
