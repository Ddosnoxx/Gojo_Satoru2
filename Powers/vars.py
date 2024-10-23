from email.policy import default
from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default="123"))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=1344569458))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP"))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="",
        ).split(None)
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="",
        ).split(None)
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default=""
        ).split(None)
    ]
    # CHROME_BIN = config("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    # CHROME_DRIVER = config("CHROME_DRIVER", default="/app/.chromedriver/bin/chromedriver")
    GENIUS_API_TOKEN = config("GENIUS_API", default=None)
    # AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API", default=None)
    DB_URI = config("DB_URI", default=None)
    DB_NAME = config("DB_NAME", default="gojo_satarou")
    BDB_URI = config("BDB_URI", default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_bots_network")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="gojo_bots_network")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE", default='Asia/Kolkata')
    BOT_USERNAME = "" # Leave it as it is
    BOT_ID = ""    # Leave it as it is
    BOT_NAME = ""  # Leave it as it is


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "7041838014:AAFb3IvM-ql_0A0UC7rxmmWWHDHnSWpIepg"
    API_ID = 24269862  # Your APP_ID from Telegram
    API_HASH = "5b1a646f8c8ed40f15af84c9b2dfa9e8"  # Your APP_HASH from Telegram
    OWNER_ID = 5154912723  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1002052189895  # Your Private Group ID for logs
    DEV_USERS = [5154912723]
    SUDO_USERS = [5154912723]
    WHITELIST_USERS = [5154912723]
    DB_URI = "mongodb+srv://v72267144:we9g1y4tiMbYdeLY@cluster0.lj7ku.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Your mongo DB URI
    DB_NAME = "Management"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = "" # Your genius API token or leave it as it is
    RMBG_API = "mL1mJVeYSgRpQpUoPewHykgh" # Your rmbg API token or leave it as it is
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "NoxBots" #Username without @
    SUPPORT_CHANNEL = "Lundlelobsdkmera" #Username without @
    VERSION = "VERSION" #Leave it as it is
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = "" #If you want your birthday module to work pass mongo db uri u can use same URI but I prefer passing a new one
    WORKERS = 8
    # CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
    # CHROME_DRIVER = "/app/.chromedriver/bin/chromedriver"
