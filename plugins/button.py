# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2:
        buttons = [
            [
                InlineKeyboardButton(text="Tutup", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2:
        buttons = [
            [
                InlineKeyboardButton(text="Channel 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Tutup", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2:
        buttons = [
            [
                InlineKeyboardButton(text="Channel 1", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Tutup", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2:
        buttons = [
            [
            ],
            [
                InlineKeyboardButton(text="Channel 1", url=client.invitelink),
                InlineKeyboardButton(text="Channel 2", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="Tutup", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2:
        buttons = [
            [
                InlineKeyboardButton(text="Channel 2", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagiɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2:
        buttons = [
            [
                InlineKeyboardButton(text="Join Channel 1", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2:
        buttons = [
            [
                InlineKeyboardButton(text="Join Channel 1", url=client.invitelink),
                InlineKeyboardButton(text="Join Channel 2", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
