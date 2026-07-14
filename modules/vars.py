import os

API_ID    = os.environ.get("API_ID", "31605369")
API_HASH  = os.environ.get("API_HASH", "f8b54f0c81481ebf1593adebb073d844")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
