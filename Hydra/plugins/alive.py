# HUH WHY U SEEING MY CODES, BAKK BSDK JALDI U KAMGER
import asyncio
from pyrogram import *
from pyrogram.types import *
from Hydra.modules.helpers.basics import edit_or_reply
from Hydra.modules.helpers.filters import command
from Hydra.utilities.misc import SUDOERS


@Client.on_message(command(["alive"]) & SUDOERS)
async def mother_chod(client: Client, message: Message):
    await edit_or_reply(message, "**🥀 I Aᴍ Aʟɪᴠᴇ Mʏ Dᴇᴀʀ Gᴇɴɪᴜs Mᴀsᴛᴇʀ ✨ ...**")



__MODULE__ = "Aʟɪᴠᴇ"
__HELP__ = f"""
**🥀 Tᴇsᴛ Yᴏᴜʀ Bᴏᴛ Wᴏʀᴋɪɴɢ Oʀ Nᴏᴛ.**

`.alive` - **Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Cʜᴇᴄᴋ**
"""
