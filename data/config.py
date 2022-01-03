# - *- coding: utf- 8 - *-
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
BOT_TOKEN = config["settings"]["token"]
ADMINS = config["settings"]["admin_id"]
if "," in ADMINS:
    ADMINS = ADMINS.split(",")
else:
    if len(ADMINS) >= 1:
        ADMINS = [ADMINS]
    else:
        ADMINS = []
        print("***** Вы не указали админ ID *****")