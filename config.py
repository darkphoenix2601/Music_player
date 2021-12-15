import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Professor MUSIC PLAYER")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/db7e9196316d0a4dfecf8.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/0f3f7be84fa65984a6169.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/5e2ae3b3421c4e64ddfa2.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/e623eef8d0095ae8de786.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/b81b94b272c3d4fa66c86.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a7ca957dfc07340df2d3f.mp4")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "Professor_Ashu_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Professer_Ashu")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Miss_AkshiV1_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Miss_AkshiV1_Updates")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "Professer_Ashu")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "Professor")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/darkphoenix2601/Music_player"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
