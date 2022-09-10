import configparser

config = configparser.RawConfigParser()
config.read("Configuration/config.ini")
class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get("common info", "baseurl")
        return url
    @staticmethod
    def get_username():
        username = config.get("common info", "username")
        return username
    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password
    @staticmethod
    def get_newusername():
        username = config.get("common info", "username2")
        return username
    @staticmethod
    def get_newpassword():
        newpassword = config.get("common info", "password2")
        return newpassword