
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# OwenUserBot - ByMisakiMey - ErdewBey

from datetime import datetime
from telethon import events
from MoonBot import OWNER_ID
from MoonBot.asisstant.events import owen
import asyncio

@owen(incoming=True, from_users=OWNER_ID, pattern="^/ping")
async def evnt (e):
    start = datetime.now()
    msg = await e.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"**Pong!!**\n `{ms} ms`")
    
    

