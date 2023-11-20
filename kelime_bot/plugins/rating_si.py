from kelime_bot import rating
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message


@Client.on_message(filters.command("reytinq"))
async def ratingsa(c:Client, m:Message):
    global rating
    metin = """⚡Qlobal Reytinq:
"""
    eklenen = 0
    puanlar = []
    for kisi in rating:
        puanlar.append(rating[kisi])
    puanlar.sort(reverse = True)
    for puan in puanlar:
        for kisi in rating:
            if puan == rating[kisi]:
                metin += f"**{kisi}** : {puan} Xal\n"
                eklenen += 50
                if eklenen == 30:
                    break
                
    await c.send_message(m.chat.id, metin)
