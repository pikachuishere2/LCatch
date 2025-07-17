# ------------------------------ IMPORTS ---------------------------------
import logging
import os
from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client, filters as f
from pyrogram.types import x

# --------------------------- LOGGING SETUP ------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("telegram").setLevel(logging.ERROR)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# ---------------------------- CONSTANTS ---------------------------------
api_id = os.getenv("API_ID", "22949712")
api_hash = os.getenv("API_HASH", "918007ea4d42bb1b3eeb509d3f99b04a")
TOKEN = os.getenv("TOKEN", "7727035867:AAFN7gPqQQHRksirYq69G5CsCmceEImy1es")
GLOG = os.getenv("GLOG", "lusst_log")
CHARA_CHANNEL_ID = os.getenv("CHARA_CHANNEL_ID", "lusst_log")
SUPPORT_CHAT_ID = os.getenv("SUPPORT_CHAT_ID", "-1002521213057")
mongo_url = os.getenv("MONGO_URL", "mongodb+srv://shreyan82683:shreyan82683@cluster0.ucwuljq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

MUSJ_JOIN = os.getenv("MUSJ_JOIN", "-1002521213057")

# Modified to support both image and video URLs
START_MEDIA = os.getenv("START_MEDIA", "https://files.catbox.moe/tz669l.jpg,https://files.catbox.moe/90v7f0.mp4").split(',')

PHOTO_URL = [
    os.getenv("PHOTO_URL_1", "https://files.catbox.moe/vynvvl.jpg"),
    os.getenv("PHOTO_URL_2", "https://files.catbox.moe/vynvvl.jpg")
]

STATS_IMG = ["https://files.catbox.moe/0yl60o.jpg"] 

SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/+Qq_DJrLZyOAxOWE1")
UPDATE_CHAT = os.getenv("UPDATE_CHAT", "https://t.me/lUst_uPdates")
SUDO = list(map(int, os.getenv("SUDO", "7824632184").split(',')))
OWNER_ID = int(os.getenv("OWNER_ID", "8043525426"))

# --------------------- TELEGRAM BOT CONFIGURATION -----------------------
command_filter = f.create(lambda _, __, message: message.text and message.text.startswith("/"))
application = Application.builder().token(TOKEN).build()
LC = Client("Shivu", api_id=api_id, api_hash=api_hash, bot_token=TOKEN)

# -------------------------- DATABASE SETUP ------------------------------
ddw = AsyncIOMotorClient(mongo_url)
db = ddw['hinata_waifu']

# Collections
user_totals_collection = db['gaming_totals']
group_user_totals_collection = db['gaming_group_total']
top_global_groups_collection = db['gaming_global_groups']
pm_users = db['gaming_pm_users']
destination_collection = db['gamimg_user_collection']
destination_char = db['gaming_anime_characters']

# -------------------------- GLOBAL VARIABLES ----------------------------
app = LC
sudo_users = SUDO
collection = destination_char
user_collection = destination_collection
x = x
# --------------------------- STRIN ---------------------------------------
locks = {}
message_counters = {}
spam_counters = {}
last_characters = {}
sent_characters = {}
first_correct_guesses = {}
message_counts = {}
last_user = {}
warned_users = {}
user_cooldowns = {}
user_nguess_progress = {}
user_guess_progress = {}
normal_message_counts = {}  

# -------------------------- POWER SETUP --------------------------------
from LCatch.unit.zyro_ban import *
from LCatch.unit.zyro_sudo import *
from LCatch.unit.zyro_react import *
from LCatch.unit.zyro_log import *
from LCatch.unit.zyro_send_img import *
from LCatch.unit.zyro_rarity import *
# ------------------------------------------------------------------------

async def PLOG(text: str):
    await app.send_message(
       chat_id=GLOG,
       text=text
   )

# ---------------------------- END OF CODE ------------------------------
