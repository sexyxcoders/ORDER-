from pyrogram.types import InlineKeyboardButton

import config
from BrandrdXMusic import app


def start_pannel(_):
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

        # ✅ ADDED API PONG BUTTON HERE
        [
            InlineKeyboardButton(text="💗 ᴀᴘɪ ᴘᴏɴɢ", callback_data="api_pong"),
        ],

        [
            InlineKeyboardButton(text="• sᴏᴜꝛᴄᴇ •", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons