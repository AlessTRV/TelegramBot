import logging
import os
import pyrogram
import datetime
import coloredlogs

from pyrogram.types import Message
from pyrogram import Client, filters, idle
from dotenv import load_dotenv

logger: logging.Logger = logging.getLogger("pyrofork")
coloredlogs.install(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", logger=logger)
logger.info("[+] Starting bot...")

load_dotenv()
api_id = 29695292
bot_token = "7373220875:AAGvL2lJkvr-bXmUBA7sjzIVS6AOC-kWSJA"
api_hash = "8b05ce00146edeeae7aafc4bea30e713"
#api_id: int = int(os.getenv("TELEGRAM_API_ID"))
#api_hash: str = os.getenv("TELEGRAM_API_HASH")
#bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN")

app = Client(name="BOT", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def ls():
    dirs = os.listdir(os.getcwd()+"/files")
    dirs.sort()
    sstr = f"|{os.getcwd()}\\files|\n"
    j = 0
    for i in dirs:
        obj = f"{os.getcwd()}/files/"+str(i)
        if os.path.isdir(obj):
            sstr += f"{j} {pyrogram.emoji.FILE_FOLDER} " + i + "\n"
        elif os.path.isfile(obj):
            sstr += f"{j} {pyrogram.emoji.PAGE_FACING_UP} " + i + "\n"
        elif os.path.islink(obj):
            sstr += f"{j} {pyrogram.emoji.LINK} " + i + "\n"
        else:
            sstr += f"[{j}][other] " + i + "\n"
            j+=1
    return sstr

@app.on_message(~filters.me & filters.command("start") & filters.private)
async def start_command(_, message:Message):
    name = message.from_user.first_name
    logger.info(f"[LOG] Start command performed by {name}")
    await message.reply(f"Hello {message.from_user.mention}!\n\nUse /cmds for commands list")


@app.on_message(~filters.me & filters.command("cmds") & filters.private)
async def cmds_command(_, message:Message):
    name = message.from_user.first_name
    logger.info(f"[LOG] Cmds command performed by {name}")
    await message.reply(f"/cmds - Show this message\n/start - Start command\n/ping - Get the bot latency\n/dev - Developer info")


@app.on_message(~filters.me & filters.command("dev") & filters.private)
async def dev_command(_, message:Message):
    name = message.from_user.first_name
    logger.info(f"[LOG] Dev command performed by {name}")
    await message.reply(f"This bot has been developed by @Peggiorincubo")

@app.on_message(~filters.me & filters.command("ls") & filters.private)
async def dev_command(_, message:Message):
    name = message.from_user.first_name
    logger.info(f"[LOG] Ls command performed by {name}")
    await message.reply(f"{ls()}")

@app.on_message(~filters.me & filters.command("ping"))
async def ping_command(_, message:Message):
    name = message.from_user.first_name
    logger.info(f"[LOG] Ping command performed by {name}")
    now: datetime = datetime.datetime.now()
    a = await message.reply_text("<blockquote>Pong!</blockquote>")
    end: datetime = datetime.datetime.now()
    ms: float = (end - now).microseconds / 1000
    await a.edit(f"<blockquote>Pong! <code>{ms}ms</code></blockquote>")

@app.on_message(~filters.me & filters.media)
async def download_media(_,message:Message):
    if message.media == None:
        return
    a = await message.reply("downloading...")
    await app.download_media(message,os.getcwd()+"/files/")
    await a.edit("downloaded !!!")



@app.on_message(~filters.me)
async def send_file_command(_,message:Message):
    if message.media != None:
        return
    name = message.from_user.first_name
    text = message.text
    logger.info(f"[LOG] send file by {name}")
    if text.startswith("/send"):
        text = text.split(" ",1)
        text.append(None)
        file = "files/"+text[1]
        if file == None:
            await message.reply("file not found")
            return
        try:
            size = os.path.getsize(file)
        except Exception as e:
            await message.reply(str(e))
        await message.reply_document(file,caption=f"size: {size}Bytes")



app.start()
logger.info("[+] Bot started as @{}".format(app.me.first_name))
idle()
