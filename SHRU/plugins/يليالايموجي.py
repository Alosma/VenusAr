from SHRU import Qrh9
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import Message
@Qrh9.ar_cmd(pattern=r"ميو")
async def forward(event):
    reply_message = event.reply_to
    if reply_message:
        if isinstance(reply_message, Message):
            reply_message = reply_message.message
        if reply_message and reply_message.entities:
            for entity in reply_message.entities:
                if entity.type == "url":
                    if "t.me/c/" in entity.url or "t.me/g/" in entity.url or "t.me/s/" in entity.url:
                        await event.client.join_chat(entity.url)
                        await event.client.send_message(entity.url, "\start")
            await forward(event)
        else:
            await event.edit("لا يوجد روابط في الرسالة")
    else:
        await event.edit("لا يوجد روابط في الرسالة")
