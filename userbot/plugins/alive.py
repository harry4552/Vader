from userbot import *
from hellbot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#-------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/2dab398583392fdf5ed79.mp4"
pm_caption = "__**☠ρøıƨøп ʙᴏᴛ☠**__\n\n"

pm_caption += (
    f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『 [{DEFAULTUSER}](tg://user?id={kraken}) 』**\n\n"
)

pm_caption += f"🛡️TELETHON🛡️ : `{version.__version__}` \n"

pm_caption += f"☠ρøıƨøп ʙᴏᴛ☠       : __**{hellversion}**__\n"

pm_caption += f"⚜️Sudo⚜️            : `{sudou}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/shinchan_the_h4ch3r)\n"

pm_caption += "🔥CREATOR🔥    : [Nub Here](https://t.me/me_izz_shreef)\n\n"

pm_caption += "    [✨REPO✨](https://github.com/harry4552/hellbot) 🔹 [📜License📜](https://github.com/harry4552/HellBot/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'hell', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add_info(
  'Zinda Hai Kya Bro?'
).add()

