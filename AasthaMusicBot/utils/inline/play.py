#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Dr_Asad_Ali
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. Yukki

from pyrogram.types import InlineKeyboardButton


def track_markup(_, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                url=f"https://t.me/Shayri_Music_Lovers",
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(text=_["PL_B_3"], url=f"https://t.me/Dr_Asad_Ali"),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], url=f"https://t.me/Alexa_Help"
            )
        ],
    ]
    return buttons


def telegram_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["PL_B_3"], switch_inline_query_current_chat=""),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], url=f"https://t.me/Alexa_Help"
            ),
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"Alexa Playlist {videoid}|{user_id}|{ptype}|a",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"Alexa Playlist {videoid}|{user_id}|{ptype}|v",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                url=f"https://t.me/Shayri_Music_Lovers",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                url=f"https://t.me/Shayri_Music_Lovers",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}",
            ),
        ],
    ]
    return buttons
