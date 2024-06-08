import os
import datetime

from pyrogram import Client, filters, idle
from dotenv import load_dotenv

print("[LOG] Starting bot...")

load_dotenv()

api_id: int = int(os.getenv("TELEGRAM_API_ID"))
api_hash: str = os.getenv("TELEGRAM_API_HASH")
bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN")

app = Client(name="BOT", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(~filters.me & filters.command("start") & filters.private)
async def start_command(app, message):
    print("[LOG] Start command performed by {}".format(message.from_user.first_name))
    await message.reply(f"Hello {message.from_user.mention}!\n\nUse /cmds for commands list")


@app.on_message(~filters.me & filters.command("cmds") & filters.private)
async def cmds_command(app, message):
    print("[LOG] Cmds command performed by {}".format(message.from_user.first_name))
    await message.reply(f"/cmds - Show this message\n/start - Start command\n/ping - Get the bot latency\n/dev - Developer info")


@app.on_message(~filters.me & filters.command("dev") & filters.private)
async def dev_command(app, message):
    print("[LOG] Help command performed by {}".format(message.from_user.first_name))
    await message.reply(f"This bot has been developed by @Peggiorincubo")


@app.on_message(~filters.me & filters.command("ping"))
async def ping_command(app, message):
    now: datetime = datetime.datetime.now()
    a = await message.reply_text("<blockquote>Pong!</blockquote>")
    end: datetime = datetime.datetime.now()
    ms: float = (end - now).microseconds / 1000
    await a.edit(f"<blockquote>Pong! <code>{ms}ms</code></blockquote>")

app.start()
print("[LOG] Bot started as @{}".format(app.me.first_name))
idle()
