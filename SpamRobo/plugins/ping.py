import os
import asyncio
import sys
import git
import heroku3
from SpamRobo import anon, anon2, anon3, anon4, anon5 , anon6, anon7, anon8, anon9, anon10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, fversion
from SpamRobo import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from SpamRobo import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime



def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@anon.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@anon2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@anon3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@anon4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@anon5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@anon6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@anon7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@anon8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@anon9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@anon10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "🏓 ᴘɪɴɢɪɴɢ ʙᴀʙʏ​..."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"» ꜰᴜᴄᴋᴇʀ ✘ sᴘᴀᴍ « `{ms}` ᴍs\n\n𝗪𝗧𝗙 !\n𝗛𝗢𝗪'𝗦 𝗧𝗛𝗜𝗦 𝗣𝗢𝗦𝗦𝗜𝗕𝗟𝗘 ?")
 
       
@anon.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@anon2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@anon3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@anon4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@anon5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@anon6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@anon7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@anon8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@anon9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@anon10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "» ʀᴇsᴛᴀʀᴛɪɴɢ ʏᴏᴜʀ sᴘᴀᴍʙᴏᴛs ʙᴀʙʏ...\n ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ꜰᴏʀ ꜰᴇᴡ sᴇᴄ ᴜɴᴛɪʟ ɪ ʀᴇsᴛᴀʀᴛ​"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await anon.disconnect()
        except Exception:
            pass
        try:
            await anon2.disconnect()
        except Exception:
            pass
        try:
            await anon3.disconnect()
        except Exception:
            pass
        try:
            await anon4.disconnect()
        except Exception:
            pass
        try:
            await anon5.disconnect()
        except Exception:
            pass
        try:
            await anon6.disconnect()
        except Exception:
            pass
        try:
            await anon7.disconnect()
        except Exception:
            pass
        try:
            await anon8.disconnect()
        except Exception:
            pass
        try:
            await anon9.disconnect()
        except Exception:
            pass
        try:
            await anon10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

@anon.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("ᴀᴅᴅɪɴɢ ɴᴇᴡ ᴄʜᴜᴛɪʏᴀ ᴀs ᴍʏ ᴀɴᴏᴛʜᴇʀ ᴏᴡɴᴇʀ​...")
        anon = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nᴀᴅᴅ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ɴᴀᴍᴇ ɪɴ ᴠᴀʀs ʙᴀʙʏ ᴇʟsᴇ ᴛᴜᴍʜᴀʀɪ ᴍᴋʙ​")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴄʜᴜᴛɪʏᴀ ᴍsɢ ᴛᴏ ᴀᴅᴅ ʜɪᴍ ᴀs ᴀɴᴏᴛʜᴇʀ ʀᴀᴍᴅɪ​...")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**ᴀᴅᴅᴇᴅ `{target}` ** ᴀs ᴍʏ ᴀɴᴏᴛʜᴇʀ ʀᴀᴍᴅɪ ᴏᴡɴᴇʀ !\nʟᴇᴛ ᴍᴇ ʀᴇsᴛᴀʀᴛ ɴᴏᴡ​...")
        heroku_var[anon] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
