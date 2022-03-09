from SpamRobo import anon, anon2, anon3, anon4, anon5, anon6, anon7, anon8, anon9, anon10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from SpamRobo import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/7bd111132fce009e4605e.jpg"

anon_Help = "» ᴊᴜꜱᴛ ᴘʀᴇꜱꜱ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴀɴᴅ ʀᴇᴀᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ «"


@anon.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@anon2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@anon3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@anon4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@anon5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@anon6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@anon7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@anon8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@anon9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@anon10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=anon_Help,
                                  buttons=[
           [
            Button.inline("• sᴩᴀᴍ •", data="spam"),
            Button.inline("• ʀᴀɪᴅ •", data="raid"),
           ],
           [
            Button.inline("• ғᴜᴄᴋ •", data="extra"),
           ],
           [    
            Button.url("• sᴜᴩᴩᴏʀᴛ •", "https://t.me/DevilsHeavenMF")
           ],
           ],
           )              

  
  
extra_msg = f"""
**ᴜsᴇʟᴇss ʜᴇʟᴩ ᴄᴏᴍᴍᴀɴᴅs**

**ʙᴏᴛ**: ᴜsᴇʟᴇss
ᴄᴏᴍᴍᴀɴᴅs :
» {hl}ping 
» {hl}alive
» {hl}restart
» {hl}addsudo <ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴄʜᴜᴛɪʏᴀ> : ᴏɴʟʏ ғᴏʀ ᴏᴡɴᴇʀs

**ʟᴇᴀᴠᴇ**: ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴩ ᴏʀ ᴄʜᴀɴɴᴇʟ
ᴄᴏᴍᴍᴀɴᴅs:
» {hl}leave <ɢʀᴏᴜᴩ/ᴄʜᴀᴛ ɪᴅ>
» {hl}leave : sᴇɴᴅ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴩ ʙᴏᴛs ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴄʜᴀᴛ.

**ᴩᴀᴄᴋ sᴩᴀᴍ**: sᴩᴀᴍ ᴛʜᴇ ᴡʜᴏʟᴇ sᴛɪᴄᴋᴇʀ ᴩᴀᴄᴋ
» {hl}packspam (ʀᴇᴩʟʏ ᴏɴ ᴀ sᴛɪᴄᴋᴇʀ)

**© [﹫ᴅᴇᴠɪʟsʜᴇᴀᴠᴇɴᴍғ](t.me/DevilsHeavenMF)**
"""

                 
raid_msg = f"""
**ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅs**


**ʀᴀɪᴅ:** ᴀᴄᴛɪᴠᴀᴛᴇ ʀᴀɪᴅ ᴏɴ ᴀ ᴜsᴇʀ ᴀɴᴅ ғᴜᴄᴋ ʜɪᴍ ʜᴀʀᴅ ᴀᴛ ɢɪᴠᴇɴ ʀᴀɴɢᴇ
ᴄᴏᴍᴍᴍᴀɴᴅs:
» {hl}raid <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ ᴏғ ᴄʜᴜᴛɪʏᴀ>
» {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴄʜᴜᴛɪʏᴀ>

**ᴅᴇʟᴀʏʀᴀɪᴅ**: ᴀᴄᴛɪᴠᴀᴛᴇ ᴅᴇʟᴀʏ ʀᴀɪᴅ ᴏɴ ᴀ ᴜsᴇʀ ᴀɴᴅ ғᴜᴄᴋ ʜɪᴍ ʜᴀʀᴅ ᴀᴛ ɢɪᴠᴇɴ ʀᴀɴɢᴇ
ᴄᴏᴍᴍᴀɴᴅs:
» {hl}delayraid <ᴅᴇʟᴀʏ> <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ ᴏғ ᴄʜᴜᴛɪʏᴀ>
» {hl}delayraid <ᴅᴇʟᴀʏ> <ᴄᴏᴜɴᴛ> <ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴄʜᴜᴛɪʏᴀ>

**ʀᴇᴩʟʏʀᴀɪᴅ:** ᴀᴄᴛɪᴠᴀᴛᴇ ʀᴇᴩʟʏ ʀᴀɪᴅ ᴏɴ ᴜsᴇʀ ᴀɴᴅ ғᴜᴄᴋ ʜɪᴍ ᴡʜᴇɴᴇᴠᴇʀ ʜᴇ ᴡɪʟʟ ᴛʀʏ ᴛᴏ ᴛᴀᴋᴇ ʀᴇᴠᴇɴɢᴇ
ᴄᴏᴍᴍᴀɴᴅs:
» {hl}replyraid <ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴄʜᴜᴛɪʏᴀ>
» {hl}dreplyraid <ᴜsᴇʀɴᴀᴍᴇ ᴏғ ᴄʜᴜᴛɪʏᴀ>

**ᴅʀᴇᴩʟʏʀᴀɪᴅ:** ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇ ʀᴇᴩʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴩʀᴇᴠɪᴏᴜsʟʏ ғᴜᴄᴋᴇᴅ ᴜsᴇʀ
ᴄᴏᴍᴍᴀɴᴅs:
» {hl}dreplyraid <ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴄʜᴜᴛɪʏᴀ>
» {hl}dreplyraid <ᴜsᴇʀɴᴀᴍᴇ ᴏғ ᴄʜᴜᴛɪʏᴀ>


**© [﹫ᴅᴇᴠɪʟsʜᴇᴀᴠᴇɴᴍғ](t.me/DevilsHeavenMF)**
"""

spam_msg = f"""
**sᴩᴀᴍ ᴄᴏᴍᴍᴀɴᴅs**

**sᴩᴀᴍ**: sᴩᴀᴍs ᴀ ᴍsɢ ғᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ ᴀɴᴅ ᴡɪʟʟ ɴᴏᴛ sᴛᴏᴩ ᴜɴᴛɪʟ ᴏʀᴅᴇʀᴇᴅ ᴛᴏ ʀᴇsᴛᴀʀᴛ ᴏʀ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴄʜᴀᴛ (ʟᴇss ᴛʜᴀɴ 100)
ᴄᴏᴍᴍᴀɴᴅs:
» {hl}spam <ᴄᴏᴜɴᴛ> <ᴛʜᴇ ᴍsɢ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴩᴀᴍ> 
» {hl}spam <ᴄᴏᴜɴᴛ> <ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍsɢ>

**ʙɪɢsᴩᴀᴍ**: sᴀᴍᴇ ᴜsᴀɢᴇ ᴀs ᴀʙᴏᴠᴇ ʙᴜᴛ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ғᴏʀ sᴩᴀᴍᴍɪɴɢ ᴍᴏʀᴇ ᴛʜᴀɴ 100
ᴄᴏᴍᴍᴀɴᴅs:
» {hl}bigspam <ᴄᴏᴜɴᴛ> <ᴛʜᴇ ᴍsɢ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴩᴀᴍ> 
» {hl}bigspam <ᴄᴏᴜɴᴛ> <ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍsɢ>

**ᴅᴇʟᴀʏsᴩᴀᴍ**: ᴋᴇᴇᴩ sᴩᴀᴍᴍɪɴɢ ᴀ ᴍsɢ ғᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ ᴀᴛ ᴛʜᴇ ᴅᴇʟᴀʏ ᴏғ ɢɪᴠᴇɴ ᴛɪᴍᴇ
command:
» {hl}delayspam <ᴅᴇʟᴀʏ> <ᴄᴏᴜɴᴛ> <ᴛʜᴇ ᴍsɢ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴩᴀᴍ> (you can reply any message if you want bot to reply that message and do spamming)
» {hl}delayspam <ᴅᴇʟᴀʏ> <ᴄᴏᴜɴᴛ> <ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍsɢ>

**pornspam**: ᴩᴏʀɴ sᴩᴀᴍ
#ᴍʏ ғᴀᴠᴏʀɪᴛᴇ
ᴄᴏᴍᴍᴀɴᴅs:
» {hl}pornspam <count> (sᴛᴀʀᴛs sᴩᴀᴍᴍɪɴɢ ᴩᴏʀɴ ɢɪғ's ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ)

**hang**: sᴩᴀᴍs ᴀ ᴍsɢ ᴡʜɪᴄʜ ғᴜᴄᴋ ᴜᴩ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀᴛ ɪɴᴛᴇʀғᴀᴄᴇ ᴀɴᴅ ʏᴏᴜʀ ᴇɴᴇᴍʏ's ᴅᴇᴠɪᴄᴇ
command:
» {hl}hang <ᴄᴏᴜɴᴛᴇʀ> 

** © [﹫ᴅᴇᴠɪʟsʜᴇᴀᴠᴇɴᴍғ](t.me/DevilsHeavenMF)**
"""                     
           
           
@anon.on(events.CallbackQuery(pattern=r"help_back"))
@anon2.on(events.CallbackQuery(pattern=r"help_back"))
@anon3.on(events.CallbackQuery(pattern=r"help_back"))
@anon4.on(events.CallbackQuery(pattern=r"help_back"))
@anon5.on(events.CallbackQuery(pattern=r"help_back"))
@anon6.on(events.CallbackQuery(pattern=r"help_back"))
@anon7.on(events.CallbackQuery(pattern=r"help_back"))
@anon8.on(events.CallbackQuery(pattern=r"help_back"))
@anon9.on(events.CallbackQuery(pattern=r"help_back"))
@anon10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            anon_Help,
            buttons=[
                [
            Button.inline("• sᴩᴀᴍ •", data="spam"),
            Button.inline("• ʀᴀɪᴅ •", data="raid"),
           ],
           [
            Button.inline("• ғᴜᴄᴋ •", data="extra"),
           ],
           [    
            Button.url("• sᴜᴩᴩᴏʀᴛ •", "https://t.me/DevilsHeavenMF")
           ],
           ],
        )           
   else:
        Alert = (
                "ᴋʏᴀ ʀᴇ ᴄʜᴜᴛɪʏᴇ ᴊᴀᴀᴋᴇ ᴋʜᴜᴅᴋᴀ ʙᴀɴᴀ ɴᴀ !"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@anon.on(events.CallbackQuery(pattern=r"spam"))
@anon2.on(events.CallbackQuery(pattern=r"spam"))
@anon3.on(events.CallbackQuery(pattern=r"spam"))
@anon4.on(events.CallbackQuery(pattern=r"spam"))
@anon5.on(events.CallbackQuery(pattern=r"spam"))
@anon6.on(events.CallbackQuery(pattern=r"spam"))
@anon7.on(events.CallbackQuery(pattern=r"spam"))
@anon8.on(events.CallbackQuery(pattern=r"spam"))
@anon9.on(events.CallbackQuery(pattern=r"spam"))
@anon10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("• ʙᴀᴄᴋ •", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "ᴋʏᴀ ʀᴇ ᴄʜᴜᴛɪʏᴇ ᴊᴀᴀᴋᴇ ᴋʜᴜᴅᴋᴀ ʙᴀɴᴀ ɴᴀ !"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@anon.on(events.CallbackQuery(pattern=r"raid"))
@anon2.on(events.CallbackQuery(pattern=r"raid"))
@anon3.on(events.CallbackQuery(pattern=r"raid"))
@anon4.on(events.CallbackQuery(pattern=r"raid"))
@anon5.on(events.CallbackQuery(pattern=r"raid"))
@anon6.on(events.CallbackQuery(pattern=r"raid"))
@anon7.on(events.CallbackQuery(pattern=r"raid"))
@anon8.on(events.CallbackQuery(pattern=r"raid"))
@anon9.on(events.CallbackQuery(pattern=r"raid"))
@anon10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("• ʙᴀᴄᴋ •", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "ᴋʏᴀ ʀᴇ ᴄʜᴜᴛɪʏᴇ ᴊᴀᴀᴋᴇ ᴋʜᴜᴅᴋᴀ ʙᴀɴᴀ ɴᴀ !"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@anon.on(events.CallbackQuery(pattern=r"extra"))
@anon2.on(events.CallbackQuery(pattern=r"extra"))
@anon3.on(events.CallbackQuery(pattern=r"extra"))
@anon4.on(events.CallbackQuery(pattern=r"extra"))
@anon5.on(events.CallbackQuery(pattern=r"extra"))
@anon6.on(events.CallbackQuery(pattern=r"extra"))
@anon7.on(events.CallbackQuery(pattern=r"extra"))
@anon8.on(events.CallbackQuery(pattern=r"extra"))
@anon9.on(events.CallbackQuery(pattern=r"extra"))
@anon10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("• ʙᴀᴄᴋ •", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "ᴋʏᴀ ʀᴇ ᴄʜᴜᴛɪʏᴇ ᴊᴀᴀᴋᴇ ᴋʜᴜᴅᴋᴀ ʙᴀɴᴀ ɴᴀ !"
            )
        await event.answer(Alert, cache_time=0, alert=True)

