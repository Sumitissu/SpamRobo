import heroku3
import asyncio
from SpamRobo import anon, anon2, anon3, anon4, anon5, anon6, anon7, anon8, anon9, anon10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, fversion
from SpamRobo import CMD_HNDLR as hl
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest
from SpamRobo import ALIVE_PIC
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
import os
import random
import sys

@anon.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@anon2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@anon3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@anon4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@anon5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@anon6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@anon7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@anon8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@anon9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@anon10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:
        fuck = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = fuck[0]
            Xd = int(bc)
            text = "ᴛʀʏɪɴɢ ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴄʜᴀᴛ..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(Xd))
                await event.edit("ʟᴇғᴛ ᴛʜᴀᴛ ғᴜᴄᴋɪɴɢ ᴜɢʟʏ ᴄʜᴀᴛ 😴")
            except Exception as e:
                await event.edit(str(e))
         
        else:
             bc = e.chat_id
             Xd = int(bc)
             text = "ᴍᴇ ɪᴢ ʟᴇᴀᴠɪɴɢ ᴛʜɪs ʟᴇʟ ɢʀᴏᴜᴩ...😜"
             if e.is_private:
                  dik = f"ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ ᴛʜɪs ʜᴇʀᴇ ʙᴀʙʏ !! \n\n {hl}leave <ᴄʜᴀɴɴᴇʟ ᴏʀ ᴄʜᴀᴛ ɪᴅ> \n {hl}leave : sᴇɴᴅ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴄʜᴀᴛ."
                  await e.reply(dik, parse_mode=None, link_preview=None )
             else:
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  try:
                      await event.client(LeaveChannelRequest(Xd))
                  except Exception as e:
                      await event.edit(str(e))
