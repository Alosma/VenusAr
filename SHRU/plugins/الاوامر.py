# WRITE  BY SHRU
# PLUGIN FOR SHRU 
# @SXYO3

from telethon import events
import random, re
from ..Config import Config

from SHRU.utils import admin_cmd

import asyncio
from SHRU import l313l
from random import choice

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus

plugin_category = "extra"
ALLOWED_USERS = [1109370707,6262533559]
rehu = [
    "قال المهدي(عجل الله فرجه):الدّينُ لمحمّد صلى الله عليه وآله وسلم والهدايةُ لعَلِيٍّ أمير المؤمنين ع، لأنها لهُ وفي عَقِبِه باقيةً إلى يومِ القيامة",
    "قال المهدي(عجل الله فرجه):إذا استغفرت الله (عز وجل) فالله يغفر لك",
    "قال المهدي(عجل الله فرجه):لا يحلّ لأحد أن يتصرّف في مال غيره بغير إذنه",
    "قال المهدي(عجل الله فرجه):إن اُستَرشدت أُرشِدتَ، وإن طَلبت وجدت",
    "قَالَ الإمام علي (عليه السلام): يَا ابْنَ آدَمَ إِذَا رَأَيْتَ رَبَّكَ سُبْحَانَهُ يُتَابِعُ عَلَيْكَ نِعَمَهُ وَأَنْتَ تَعْصِيهِ فَاحْذَرْهُ",
    "قَالَ الإمام علي (عليه السلام): الصَّبْرُ صَبْرَانِ صَبْرٌ عَلَى مَا تَكْرَهُ وَصَبْرٌ عَمَّا تُحِبُّ",
    "قَالَ الإمام علي (عليه السلام): لَا يَكُونُ الصَّدِيقُ صَدِيقاً حَتَّى يَحْفَظَ أَخَاهُ فِي ثَلَاثٍ فِي نَكْبَتِهِ وَغَيْبَتِهِ وَوَفَاتِهِ",
    "قال الإمام الصادق(عليه السلام): اكتبوا فإنكم لا تحفظون حتى تكتبو",
    "قال الإمام الصادق(عليه السلام): ركعة يصليها الفقيه أفضل من سبعين ألف ركعة يصليها العابد",
    "قال الإمام الصادق(عليه السلام): طلب العلم فريضة من فرائض الله",
    "عن رسول الله (صلى الله عليه وآله): الْبَخِيلُ‏ حَقّاً مَنْ ذُكِرْتُ عِنْدَهُ فَلَمْ يُصَلِّ عَلَيَّ",
    "عن رسول الله (صلى الله عليه وآله): مَنْ أَتَانِي زَائِراً كُنْتُ شَفِيعَهُ‏ يَوْمَ‏ الْقِيَامَة",
    "عن رسول الله (صلى الله عليه وآله): بُغْضُ‏ عَلِيٍ‏ كُفْرٌ وَ بُغْضُ بَنِي هَاشِمٍ نِفَاقٌ",
    "عن الامام علي (عليه السلام) قال : أعظم الذنوب ما استخف به صاحبه",
    "عن الامام علي (عليه السلام) قال : إذا قويت فاقو على طاعة الله، وإذا ضعفت فاضعف في معصيته",
    "عن الامام علي (عليه السلام) قال : أعداؤك ثلاثة: عدوك، وصديق عدوك، وعدو صديقك",
    "عن الامام علي (عليه السلام) قال : لا غنى كالعقل، ولا فقر كالجهل، ولا ميراث كالأدب",
    "عن الامام علي (عليه السلام) قال : لسانك حصانك، إن صنته صانك",
]
@l313l.ar_cmd(pattern="الاوامر(?:\s|$)([\s\S]*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        SX9OO = random.choice(rehu)
        await event.edit(
        f"• قـائـمـة اوامـر سـورس الـسـاحـر\n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n〈`.م1`〉⇦اوامـر الأدمـن\n〈`.م2`〉⇦ اوامـر الـمـجـمـوعـة\n〈`.م3`〉  ⇦ اوامـر الـتـرحـيـب و الردود\n〈`.م4`〉 ⇦ حـمـاية خـاص والتـلـغـراف\n〈`.م5`〉  ⇦ اوامـر الـمـنـشـن و الانـتـحـال\n〈`.م6`〉 ⇦ اوامـر الـتـحـمـيـل\n〈`.م7`〉 ⇦ اوامـر الـمـنـع و الـقـفـل\n〈`.م8`〉  ⇦ اوامـر الـتـنـظـيـف و الـتـكـرار\n〈`.م9`〉 ⇦ اوامـر الـفـارات\n〈`.م10`〉⇦اوامـر الـوقـتـي و الـتـشـغـيـل\n〈`.م11`〉 ⇦ اوامـر الـكـشـف و الـروابـط\n〈`.م12`〉 ⇦ اوامـر الـمـساعـدة والإذاعـة\n〈`.م13`〉 ⇦ اوامـر الارسـال والاذكـار\n〈`.م14`〉 ⇦ اوامـر الـمــصـقـات وكـوكـل\n〈`.م15`〉 ⇦ اوامـر الـتسـلـيـة و المـيـمـز\n〈`.م16`〉⇦ اوامـر الصـيـغ والــهـات\n〈`.م17`〉⇦ اوامـر الـتـمـبلـر والزغـرفة\n〈`.م18`〉 ⇦اوامـر الـحـسـاب والـترفـيـه\n〈`.م19`〉 ⇦ اوامـر الـمـيـوزك\n〈`.م20`〉 ⇦ اوامـر بـصـمـات الـمـيـمـز\n〈`.م21`〉 ⇦ اوامـر تـجـمـيـع الـنـقـاط\n〈`.م22`〉 ⇦ اوامـر الـسـورس الـمـمـيـز  \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n{SX9OO}")

@l313l.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الادمن لسورس الساحر **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحظر` )\n- ( `.اوامر الكتم` )\n- ( `.اوامر التثبيت` )\n- ( `.اوامر الاشراف` )\n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)
		
@l313l.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المجـموعه لسورس الساحر **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التفليش` )\n- ( `.اوامر المحذوفين` )\n- ( `.اوامر الكروب` )\n- ( `.اوامر السب` )\n\n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)

@l313l.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـترحيب والـردود **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترحيب` )\n- ( `.اوامر الردود` )\n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)
@l313l.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر حـماية الخاص والتلكراف **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحماية` )\n- ( `.اوامر التلكراف` ) \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)
@l313l.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـمنشن والانتحال **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)

@l313l.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التحميل والترجمه **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر النطق` )\n- ( `.اوامر التحميل` )\n- ( `.اوامر الترجمة` ) \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)

@l313l.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر القفل والمنع **:\n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر القفل` )\n- ( `.اوامر الفتح` )\n- ( `.اوامر المنع` ) \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)

@l313l.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التكرار والتنظيف **:\n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التكرار` )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)

@l313l.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة التخصيص والفارات **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التخصيص` )\n لتغير الصور والكلايش كل من الحماية والفحص والبنك\n- ( `.اوامر الفارات` )\n - لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها\n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
		)

@l313l.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الوقتي والتشغيل **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الاسم` )\n- ( `.اوامر البايو` )\n- ( `.اوامر الكروب الوقتي` )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)	

@l313l.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الكـشف و الروابط **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الكشف` )\n- ( `.اوامر الروابط` ) \n\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)
@l313l.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المساعدة  **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الوقت والتاريخ` )\n- ( `.اوامر كورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر مساعدة` )\n- ( `.اوامر الاذاعه` ) \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)
@l313l.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الارسال **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.امر الصورة الذاتية` )\n- ( `.اوامر التحذيرات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` ) \n- ( `.اوامر الاذكار` )\n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)
@l313l.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الملصقات وكوكل **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر كوكل` )\n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)

@l313l.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التسلية والتحشيش **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n- ( `.اوامر الميمز` )\n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)

@l313l.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر تحويل الصيغ و الجهات **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
)

@l313l.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الحساب و الترفيه **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترفيه` )\n- ( `.اوامر الحساب` ) \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"

)

@l313l.ar_cmd(
    pattern="م19",
    command=("م19", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر الميوزك والتشغيل 🎵\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n᯽︙ اختر احدى هذه الاوامر\n ᯽︙ قبل أستخدام هذه الاوامر يجب تفعيل المود بكتابة ألامر ( `.ميوزك تفعيل` ) \n- ( `.تشغيل_المكالمة` )\n- لتشغيل المحادثة الصوتيه\n- ( `.انهاء_المكالمة` )\n-لأنهاء المحادثه الصوتية \n- ( `.دعوة` )\n- بالرد على الشخص لدعوته الى المكالمة \n- ( `.معلومات_المكالمة` )\n- لعرض عنوان المكالمة وعدد لاشخاص الموجودين فيها \n- ( `.تسمية_المكالمة` )\n- لتغير عنوان المكالمة \n- ( `.انضمام` )\n- للأنضمام الى المحادثة الصوتية\n- ( `.مغادرة` )\n- لمغادرة المحادثة الصوتية \n- ( `.تشغيل` )\n-بالرد على رابط اليوتيوب او كتابة الامر مع رابط ليوتيوب لتشغيل الاغنيه \n- ( `.قائمة_التشغيل` )\n- لعرض قائمة التشغيل \n- ( `.ايقاف_مؤقت` )\n - لأيقاف الاغنية الحالية مؤقتا \n- ( `.استمرار` )\n -لأستمرار الاغنيه التي تم ايقافها \n- ( `.تخطي` )\n- لتخطي الاغنيه وتشغيل الاغنيه الموجوده في قائمة التشغيل \n\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"



)

@l313l.ar_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر بصمات الميمز **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.بصمات ميمز` )\n- ( `.بصمات ميمز2` )\n- ( `.بصمات ميمز3` )\n- ( `.بصمات ميمز4` )\n- ( `.بصمات ميمز5` )\n- ( `.بصمات انمي` ) \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"

)

@l313l.ar_cmd(
    pattern="م21$",
    command=("م21", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر تجميع النقاط **:\n 𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التجميع` ) \n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"

)
@l313l.ar_cmd(
    pattern="م22$",
    command=("م22", plugin_category),
)
async def _(event):
    if event.sender_id not in ALLOWED_USERS:
        await event.edit("لا يمكنك استعمال هذا الامر!!")
        return

    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قـائـمـة اوامـر الـسـورس الـمـمـيـز :\n𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n᯽︙ اختر احدى هذه القوائم\n-( `.اوامر الصيد` ) \nn𓇻ـــــــــــــــــــــــــــ※ــــــــــــــــــــــــــــــ𓇻\n⌔︙CH : @SXYO3"
        )
