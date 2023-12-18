from telethon import events 
import time 
import asyncio 
from MoonBot.events import register

@register(outgoing=True,pattern="^.[Ss]iri")

async def komut(event):
        await event.edit("**Alışkanlık İşte**\n __Botumuzun İsmi Değişti Unuttun mu Siri Yazmak Yerine__ `.owen` __Yazmalısın.__\n \n**Gerekli Açıklama:** t.me/OwenMoonBot/65 \n MoonBot Kanalı: @OwenMoonBot\nPlugin Kanalı: @OwenPlugin")

@register(outgoing=True,pattern="^.[Ee]pic")

async def komut(event):
        await event.edit("**Alışkanlık İşte**\n __Botumuzun İsmi Değişti Unuttun mu Epic Yazmak Yerine__ `.owen` __Yazmalısın.__\n \n**Gerekli Açıklama:** https://t.me/OwenMoonBot/80 \n MoonBot Kanalı: @OwenMoonBot\nPlugin Kanalı: @OwenPlugin")
