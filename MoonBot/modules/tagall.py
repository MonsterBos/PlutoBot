# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# OwenMoonBot - jackdanielssx

# @NaytSeyd tarafından portlanmıştır.
#

from telethon.tl.types import ChannelParticipantsAdmins
from MoonBot import CMD_HELP, bot
from MoonBot.events import register
from MoonBot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from MoonBot.language import get_value
LANG = get_value("tagall")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.tagall$")
async def _(event):
    if event.fwd_from:
        return
    mentions = "@tag"
    chat = await event.get_input_chat()
    leng = 0
    async for x in bot.iter_participants(chat):
        if leng < 4092:
            mentions += f"[\u2063](tg://user?id={x.id})"
            leng += 1
    await event.reply(mentions)
    await event.delete()

@register(outgoing=True, pattern="^.admin")
async def _(event):
    if event.fwd_from:
        return
    mentions = "@admin"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f"[\u2063](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

CmdHelp('tagall').add_command(
    'tagall', None, LANG['TA1']
).add_command(
    'admin', None, LANG['TA2']
).add()
