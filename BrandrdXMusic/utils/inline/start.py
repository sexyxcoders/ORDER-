from pyrogram.types import InlineKeyboardButton

import config
from BrandrdXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❖ ᴛᴧᴘ тᴏ sᴇᴇ ᴍᴧɢɪᴄ ❖",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="• ʜᴇʟᴘ •", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="• sᴇᴛ •", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="💗 API PONG", callback_data="yt_api),
        ],
        [
            InlineKeyboardButton(text="• sᴏᴜꝛᴄᴇ •", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons