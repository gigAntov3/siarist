import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

SUPPORT_LINK = os.getenv("SUPPORT_LINK")