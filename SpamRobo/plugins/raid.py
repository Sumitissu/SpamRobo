
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from SpamRobo import anon, anon2, anon3, anon4, anon5 , anon6, anon7, anon8, anon9, anon10, SUDO_USERS, OWNER_ID
from resources.data import RAID, REPLYRAID, ANONX
from SpamRobo import CMD_HNDLR as hl


que = {}


@anon.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@anon2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@anon3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@anon4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@anon5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@anon6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@anon7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@anon8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@anon9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@anon10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}raid <count> <Username of User>\n\n{hl}raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Anonymous = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Anonymous) == 2:
            user = str(Anonymous[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in ANONX:
                text = f"ɪ ᴡɪʟʟ ɴᴇᴠᴇʀ sᴛᴀʀᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʙᴀʙʏ, sᴏʀʀʏ ᴀɴᴅ ғᴜᴄᴋ ᴏғғ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ʏᴏᴜ ʙʟᴏᴏᴅʏ ᴍᴏᴛʜᴇʀғᴜᴄᴋᴇʀ ᴛʀʏɪɴɢ ᴛᴏ ᴛᴇᴀᴄʜ ᴍᴇ ʙᴇᴛʀᴀʏᴀʟ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ʜᴇʜᴇ, sᴏʀʀʏ ʙᴀʙʏ ᴍʏ ʙʟᴏᴏᴅʏ ᴏᴡɴᴇʀ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴋɪᴅ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Anonymous[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in ANONX:
                text = f"ɪ ᴡɪʟʟ ɴᴇᴠᴇʀ sᴛᴀʀᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʙᴀʙʏ, sᴏʀʀʏ ᴀɴᴅ ғᴜᴄᴋ ᴏғғ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ʏᴏᴜ ʙʟᴏᴏᴅʏ ᴍᴏᴛʜᴇʀғᴜᴄᴋᴇʀ ᴛʀʏɪɴɢ ᴛᴏ ᴛᴇᴀᴄʜ ᴍᴇ ʙᴇᴛʀᴀʏᴀʟ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ʜᴇʜᴇ, sᴏʀʀʏ ʙᴀʙʏ ᴍʏ ʙʟᴏᴏᴅʏ ᴏᴡɴᴇʀ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴋɪᴅ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Anonymous[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@anon.on(events.NewMessage(incoming=True))
@anon2.on(events.NewMessage(incoming=True))
@anon3.on(events.NewMessage(incoming=True))
@anon4.on(events.NewMessage(incoming=True))
@anon5.on(events.NewMessage(incoming=True))
@anon6.on(events.NewMessage(incoming=True))
@anon7.on(events.NewMessage(incoming=True))
@anon8.on(events.NewMessage(incoming=True))
@anon9.on(events.NewMessage(incoming=True))
@anon10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@anon.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@anon2.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@anon3.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@anon4.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@anon5.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@anon6.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@anon7.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@anon8.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@anon9.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@anon10.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}replyraid <Username of User>\n\n{hl}replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        Anonymous = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        fuckx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Anonymous[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in ANONX:
                text = f"ɪ ᴡɪʟʟ ɴᴇᴠᴇʀ sᴛᴀʀᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʙᴀʙʏ, sᴏʀʀʏ ᴀɴᴅ ғᴜᴄᴋ ᴏғғ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"ʏᴏᴜ ʙʟᴏᴏᴅʏ ᴍᴏᴛʜᴇʀғᴜᴄᴋᴇʀ ᴛʀʏɪɴɢ ᴛᴏ ᴛᴇᴀᴄʜ ᴍᴇ ʙᴇᴛʀᴀʏᴀʟ"            
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"ʜᴇʜᴇ, sᴏʀʀʏ ʙᴀʙʏ ᴍʏ ʙʟᴏᴏᴅʏ ᴏᴡɴᴇʀ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴋɪᴅ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴩʟʏʀᴀɪᴅ ʙᴀʙʏ, ɴᴏᴡ ʟᴇᴛ ᴛʜᴀᴛ ғᴜᴄᴋᴇʀ ᴛʏᴩᴇ ᴀ ᴡᴏʀᴅ"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in ANONX:
                text = f"ɪ ᴡɪʟʟ ɴᴇᴠᴇʀ sᴛᴀʀᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʙᴀʙʏ, sᴏʀʀʏ ᴀɴᴅ ғᴜᴄᴋ ᴏғғ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"ʏᴏᴜ ʙʟᴏᴏᴅʏ ᴍᴏᴛʜᴇʀғᴜᴄᴋᴇʀ ᴛʀʏɪɴɢ ᴛᴏ ᴛᴇᴀᴄʜ ᴍᴇ ʙᴇᴛʀᴀʏᴀʟ"
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"ʜᴇʜᴇ, sᴏʀʀʏ ʙᴀʙʏ ᴍʏ ʙʟᴏᴏᴅʏ ᴏᴡɴᴇʀ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴋɪᴅ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴩʟʏʀᴀɪᴅ ʙᴀʙʏ, ɴᴏᴡ ʟᴇᴛ ᴛʜᴀᴛ ғᴜᴄᴋᴇʀ ᴛʏᴩᴇ ᴀ ᴡᴏʀᴅ"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@anon.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@anon2.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@anon3.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@anon4.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@anon5.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@anon6.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@anon7.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@anon8.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@anon9.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@anon10.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
async def _(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}dreplyraid <Username of User>\n\n{hl}dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Anonymous = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Anonymous[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "ᴇɴᴊᴏʏ ᴋɪᴅ ɪ ᴡɪʟʟ ɴᴏᴛ ғᴜᴄᴋ ʏᴏᴜ ғʀᴏᴍ ɴᴏᴡ ᴏɴ"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "ᴇɴᴊᴏʏ ᴋɪᴅ ɪ ᴡɪʟʟ ɴᴏᴛ ғᴜᴄᴋ ʏᴏᴜ ғʀᴏᴍ ɴᴏᴡ ᴏɴ"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
@anon.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@anon2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@anon3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@anon4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@anon5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@anon6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@anon7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@anon8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@anon9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@anon10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
async def _(event):
   usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗘𝗟𝗔𝗬𝗥𝗔𝗜𝗗\n\nCommand:\n\n{hl}delayraid <delay> <count> <Username of User>\n\n{hl}delayraid <delay> <count> <reply to a User>\n\nCount and Sleeptime must be a integer."        
   if event.sender_id in SUDO_USERS:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         Anonymous = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(Anonymous) == 3:
             user = str(Anonymous[2])
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in ANONX:
                    text = f"ɪ ᴡɪʟʟ ɴᴇᴠᴇʀ sᴛᴀʀᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʙᴀʙʏ, sᴏʀʀʏ ᴀɴᴅ ғᴜᴄᴋ ᴏғғ"
                    await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) == OWNER_ID:
                text = f"ʏᴏᴜ ʙʟᴏᴏᴅʏ ᴍᴏᴛʜᴇʀғᴜᴄᴋᴇʀ ᴛʀʏɪɴɢ ᴛᴏ ᴛᴇᴀᴄʜ ᴍᴇ ʙᴇᴛʀᴀʏᴀʟ"
                await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) in SUDO_USERS:
                    text = f"ʜᴇʜᴇ, sᴏʀʀʏ ʙᴀʙʏ ᴍʏ ʙʟᴏᴏᴅʏ ᴏᴡɴᴇʀ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴋɪᴅ."
                    await event.reply(text, parse_mode=None, link_preview=None )
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(Anonymous[1])
                 sleeptimet = sleeptimem = float(Anonymous[0])
                 for _ in range(counter):
                      reply = random.choice(RAID)
                      caption = f"{username} {reply}"
                      async with event.client.action(event.chat_id, "typing"):
                          await event.client.send_message(event.chat_id, caption)
                          await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in ANONX:
                       text = f"ɪ ᴡɪʟʟ ɴᴇᴠᴇʀ sᴛᴀʀᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʙᴀʙʏ, sᴏʀʀʏ ᴀɴᴅ ғᴜᴄᴋ ᴏғғ"
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) == OWNER_ID:
                       text = f"ʏᴏᴜ ʙʟᴏᴏᴅʏ ᴍᴏᴛʜᴇʀғᴜᴄᴋᴇʀ ᴛʀʏɪɴɢ ᴛᴏ ᴛᴇᴀᴄʜ ᴍᴇ ʙᴇᴛʀᴀʏᴀʟ"
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) in SUDO_USERS:
                       text = f"ʜᴇʜᴇ, sᴏʀʀʏ ʙᴀʙʏ ᴍʏ ʙʟᴏᴏᴅʏ ᴏᴡɴᴇʀ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴋɪᴅ."
                       await event.reply(text, parse_mode=None, link_preview=None )
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(Anonymous[0])
                   counter = int(Anonymous[1])
                   for _ in range(counter):
                        reply = random.choice(RAID)
                        caption = f"{username} {reply}"
                        async with event.client.action(event.chat_id, "typing"):
                             await event.client.send_message(event.chat_id, caption)
                             await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)
