#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Dr_Asad_Ali
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. Yukki

from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from AasthaMusicBot import app
from AasthaMusicBot.misc import SUDOERS
from AasthaMusicBot.utils.database import add_off, add_on
from AasthaMusicBot.utils.decorators.language import language

# Commands
MAINTENANCE_COMMAND = get_command("MAINTENANCE_COMMAND")


@app.on_message(filters.command(MAINTENANCE_COMMAND) & SUDOERS)
@language
async def maintenance(client, message: Message, _):
    usage = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        user_id = 1
        await add_on(user_id)
        await message.reply_text(_["maint_2"])
    elif state == "disable":
        user_id = 1
        await add_off(user_id)
        await message.reply_text(_["maint_3"])
    else:
        await message.reply_text(usage)
