from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
       f"""π Hi {message.from_user.first_name}!

β¨ I am vc Music Player bot. 

π₯³ I can play music in your Telegram Group's Voice Chatπ

βοΈ Use these buttons below to know more. π""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Source Code π", url="https://github.com/Error-Shivansh/VCMusicBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π¬ King π¬", url="https://t.me/Royal_King7"
                    ),
                    InlineKeyboardButton(
                        "π£  Devloper π£", url="https://t.me/Royal_King7"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β Close β", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**death:** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πΆ Search πΆ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "β Close β", callback_data="close"
                    )
                ]
            ]
        )
    )
