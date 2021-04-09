from os import environ

# To use manual values, change these
default_bot_token = "1770841107:AAF_wk6me4qs54XqdLCE-KQao5-eKalBufo"
default_sudo_chat_id =  -1001299214423
default_owner_id = 757533521

# Don't change these value
bot_token = environ.get("BOT_TOKEN", default_bot_token)
sudo_chat_id = int(environ.get("SUDO_CHAT_ID", default_sudo_chat_id))
owner_id = int(environ.get("OWNER_ID", default_owner_id))
