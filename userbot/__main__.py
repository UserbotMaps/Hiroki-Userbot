# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

from telethon.tl.functions.channels import InviteToChannelRequest
from userbot import ALIVE_NAME, BOT_USERNAME, BOT_VER, BOTLOG_CHATID, LOGS, UPSTREAM_REPO_BRANCH, Hiroblacklist, bot
from userbot.modules import ALL_MODULES
from userbot.utils.tools import hadeh_ajg
try:
    bot.start()
    user = bot.get_me()
    Hiroblacklist = requests.get(
        "https://raw.githubusercontent.com/UserbotMaps/hiroblack/master/Hiroblacklist.json"
    ).json()
    if user.id in Hiroblacklist:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE ORANG KEK LU.\nCredits: @Bisubiarenak"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Jika {ALIVE_NAME} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/hiroshisupport")
LOGS.info(
    f"🔥Hiroshi-Userbot🔥 ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN!]")


async def vegeta_ubot_on()::
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(BOTLOG_CHATID, "🔥 **Hiroshi Userbot Berhasil Diaktifkan**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 3.1.0@Hiroshi-Userbot\n➠ **Ketik** `.ping` **Untuk Mengecheck Bot**\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @bombleebas ")
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

bot.loop.run_until_complete(check_alive())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars tidak terisi, Memulai Membuat BOT Otomatis di @Botfather..."
    )
    bot.loop.run_until_complete(hadeh_ajg())
bot.loop.run_until_complete(vegeta_ubot_on())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
