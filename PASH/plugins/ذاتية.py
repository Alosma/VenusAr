from PASH import Alosma
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from telethon import events
from PASH import *
#ها يالفاشل شعدك داخل هنا 🫣 اعتمد ع نفسك لتخلي سورس الفينوس مصدر طشت سورسك
AlAlosma_Asbo3 = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}

@Alosma.on(admin_cmd(pattern="(جلب الصورة|جلب الصوره|ذاتيه|ذاتية|حفظ)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    ‏z1zzzzzzz1 = await event.get_reply_message()
    pic = await ‏z1zzzzzzz1.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم حفظ الصـورة بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
- CH: @xxx_Venus
- Dev: @‏z1zzzzzzz1
  """,
    )
    await event.delete()
#By @xxx_Venus For You 🌹
@Alosma.on(admin_cmd(pattern="(الذاتية تشغيل|ذاتية تشغيل)"))
async def reda(event):
    if gvarstatus ("savepicforme"):
        return await edit_delete(event, "**᯽︙حفظ الذاتيات مفعل وليس بحاجة للتفعيل مجدداً **")
    else:
        addgvar("savepicforme", "reda")
        await edit_delete(event, "**᯽︙تم تفعيل ميزة حفظ الذاتيات بنجاح ✓**")
 
@Alosma.on(admin_cmd(pattern="(الذاتية تعطيل|ذاتية تعطيل)"))
async def Reda_Is_Here(event):
    if gvarstatus ("savepicforme"):
        delgvar("savepicforme")
        return await edit_delete(event, "**᯽︙تم تعطيل حفظت الذاتيات بنجاح ✓**")
    else:
        await edit_delete(event, "**᯽︙انت لم تفعل حفظ الذاتيات لتعطيلها!**")

def joker_unread_media(message):
    return message.media_unread and (message.photo or message.video)

async def Hussein(event, caption):
    media = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    lMl10l_date = event.date.strftime("%Y-%m-%d")
    lMl10l_day = AlAlosma_Asbo3[event.date.strftime("%A")]
    await bot.send_file(
        "me",
        media,
        caption=caption.format(sender.first_name, sender_id, lMl10l_date, lMl10l_day),
        parse_mode="markdown"
    )
    os.remove(media)

@Alosma.on(events.NewMessage(func=lambda e: e.is_private and joker_unread_media(e) and e.sender_id != bot.uid))
async def Reda(event):
    if gvarstatus("savepicforme"):
        caption = """**
           🗿  غير مبري الذمة اذا استعملته للأبتزاز  🗿
🗿 تم حفظ الذاتية بنجاح ✓
🗿 تم الصنع : @xxx_Venus
🗿 أسم المرسل : [{0}](tg://user?id={1})
🗿  تاريخ الذاتية : `{2}`
🗿  أرسلت في يوم `{3}`
       🗿    AlAlosma    🗿
        **"""
        await Hussein(event, caption)