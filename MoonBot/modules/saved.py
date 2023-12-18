# OwenMoonBot - ErdewBey - Midy
import asyncio
import telethon
from MoonBot.events import register
from telethon import events
from MoonBot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from MoonBot.language import get_value
LANG = get_value("saved")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.saved")
async def tm(event):
  if event.is_reply:
    mesaj = await event.get_reply_message()
  else:
    await event.edit(LANG["REPLY_MESSAGE"])
    return
  await event.client.forward_messages("me", mesaj)
  await event.edit(LANG["SUCCESSFUL"])
  
CmdHelp('saved').add_command('saved', LANG['S1'], LANG['S2']).add(),
