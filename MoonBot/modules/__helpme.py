# Copyright (C) 2021 Erdem Bey.
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# MoonBot - jackdanielssx

# @Qulec tarafından yazılmıştır.
# Thanks @Spechide.

from MoonBot import BOT_USERNAME
from MoonBot.events import register

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("__helpme")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.yard[iı]m|^.help")
async def yardim(event):
    tgbotusername = BOT_USERNAME
    if tgbotusername is not None:
        results = await event.client.inline_query(
            tgbotusername,
            "@OwenUserBot"
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    else:
        await event.edit(LANG["NO_BOT"])
