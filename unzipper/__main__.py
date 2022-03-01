
import os

from pyrogram import idle
from . import unzipperbot
from .helpers_nexa.unzip_help import check_logs
from config import Config

if __name__ == "__main__" :
    print("""
||| Unzipper Bot |||
Copyright (c) 2021 Itz-fork
""")
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    unzipperbot.start()
    print("Checking Log Channel ...")
    check_logs()
    print("Bot is active Now! Join @NexaBotsUpdates")
    idle()