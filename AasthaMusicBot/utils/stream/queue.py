#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Dr_Asad_Ali
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. Yukki

from config import autoclean, chatstats, userstats
from AasthaMusicBot.misc import db


async def put_queue(
    chat_id,
    original_chat_id,
    file,
    title,
    duration,
    user,
    vidid,
    user_id,
    stream,
):
    title = title.title()
    put = {
        "title": title,
        "dur": duration,
        "streamtype": stream,
        "by": user,
        "chat_id": original_chat_id,
        "file": file,
        "vidid": vidid,
    }
    db[chat_id].append(put)
    autoclean.append(file)
    vidid = "telegram" if vidid == "soundcloud" else vidid
    to_append = {"vidid": vidid, "title": title}
    if chat_id not in chatstats:
        chatstats[chat_id] = []
    chatstats[chat_id].append(to_append)
    if user_id not in userstats:
        userstats[user_id] = []
    userstats[user_id].append(to_append)
    return


async def put_queue_index(
    chat_id,
    original_chat_id,
    file,
    title,
    duration,
    user,
    vidid,
    stream,
):
    put = {
        "title": title,
        "dur": duration,
        "streamtype": stream,
        "by": user,
        "chat_id": original_chat_id,
        "file": file,
        "vidid": vidid,
    }
    db[chat_id].append(put)
