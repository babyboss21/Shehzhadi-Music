import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("14928190"))
API_HASH = os.getenv("3f10b4f56ee7b0dceb203a252ea18467")
SESSION = os.getenv("BQChtOMjD8yawLoXTdXbD1XkSX6z_5NG0ts45oWolpVld5mFYKThpUO_AZzp1x2JtlWBKkZMISY7FGX--D1iOa-6oPhRL4kqH0C65QDoy3grj76jKCLbzLdxJEHERtplnXEo89boI-0SK1_yarL5XnP82q5TZc_tRpB6fi2FXQ7v8GaJji61x3PZ88JLHp35ejkGZsRWdMmDhx-raz-kOgpLKTGfosbhb4eL0gj68KVyI2DT2e80JfBXEm1MEx10SUu4xzwUv77jrA0Zw1iaFIo58CHYBSnWEDWMtYHCnUqvasC196W4AD-_Y0SKSGw63BtArwE6w7U5ZQOp3OdZ3F96AAAAAS_7l40A")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)
