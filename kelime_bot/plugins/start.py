from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕Qrupa Əlavə Et➕", url=f"http://t.me/sozoyunurobot?startgroup=new")
    ],
    [
        InlineKeyboardButton("👑𝐎𝐰𝐧𝐞𝐫", url="t.me/B9SSD7"),
        InlineKeyboardButton("🆘𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="t.me/bossbotsazhelp"),
    ]
])


START = """
**👋Salam, Bota Xoş Gəldin Bu Bot İlə Söz Tapmaq Oyunu Oynaya Bilərsiniz**

✅Botun İstifadə Qaydasını Öyrənmək Üçün /help Əmrindən İstifadə Edin
"""

HELP = """
**⚡Botun Əmrləri**


🎮 /game - Oyunu Başladar
♻️ /pass - Sözü Dəyişər
🌐 /reytinq - Global Reytinqi Göstərər
❌ /stop - Oyunu Sonlandırar
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/16d05ef016aa0650172ca.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/16d05ef016aa0650172ca.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("game")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**🎮Oyun Artıq Davam Edir\n❌Oyunu Sonlandırmaq Üçün /stop Yaza Bilərsiniz")
    else:
        await m.reply(f"**🎮Oyun {m.from_user.mention}** Tərəfindən! Başladıldı\n\n⚡Uğurlar", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯Raund : {oyun[m.chat.id]['round']}/30
📝Söz :   <code>{kelime_list}</code>
💰Qazandığın Xal: 50
🔎İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻Uzunluq : {int(len(kelime_list)/2)} 

✏️Qarışıq Hərflərdən İbarət Sözü Tapın 
        """
        await c.send_message(m.chat.id, text)
        
