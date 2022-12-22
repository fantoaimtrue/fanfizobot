import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
NGROK_TOKEN = str(os.getenv("NGROK_TOKEN"))

admins_id = [
    '571104053',
]