from os import getenv
from dotenv import load_dotenv
import asyncio  
from pyrogram import Client
from pyrogram.errors import FloodWait
import datetime
import pytz

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH") 
STRING = getenv("STRING_SESSION", None)
PING_CHANNEL= int(getenv("PING_CHANNEL", None))
BOT_LIST = [x.strip() for x in getenv("BOT_LIST").split(" ")]
MSG_ID=int(getenv("MESSAGE_ID",None))
TIME = 600

loop = asyncio.get_event_loop()
app = Client(
            "Stranger" , 
            api_id=API_ID , 
            api_hash=API_HASH, 
            session_string=STRING
            )


async def ping_check():
    await app.start()
    while True:
        TEXT = "✨ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴄᴇ ɴᴇᴛᴡᴏʀᴋ ʙᴏᴛ's sᴛᴀᴛᴜs ᴄʜᴀɴɴᴇʟ"
        TEXT += f"\n\n ❄️ ʜᴇʀᴇ ɪs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ's ᴡʜɪᴄʜ ᴡᴇ ᴏᴡɴ ᴀɴᴅ ᴛʜᴇɪʀ sᴛᴀᴛᴜs (ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ), ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ᴋᴇᴇᴘ ᴜᴘᴅᴀᴛɪɴɢ ᴏɴ ᴇᴠᴇʀʏ 10 ᴍɪɴᴜᴛᴇ." 
        for bot in BOT_LIST:
            try:
                TEXT += f"\n\n ╭⎋ Bot Name: @{bot}"
                await app.send_message(f"@{bot}","/ping")
                await asyncio.sleep(4)
                messages = app.get_chat_history(f"@{bot}",limit=1)
                async for message in messages:
                    msg = message.text
                if msg == "/ping":
                    TEXT += f"\n ╰⊚ Bot Status: sʟᴇᴇᴘɪɴɢ 💤"
                else:
                    TEXT += f"\n ╰⊚ Bot Status: ᴀʟɪᴠᴇ ✨"
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except Exception as e:
                print(f"Failed to send ping to {bot}: {e}")
        sp = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
        date = sp.strftime("%d %b %Y")
        time = sp.strftime("%I : %M : %S %p")
        TEXT += f"\n\n--Last checked on--: \n{date}\n{time}"
        await app.edit_message_text(PING_CHANNEL, MSG_ID, TEXT)
        await asyncio.sleep(TIME)  # Wait for 5 minutes

if __name__== "__main__":
    loop.run_until_complete(ping_check())