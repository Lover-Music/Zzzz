import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from LoverMusic import LOGGER, app, userbot
from LoverMusic.core.call import LoverMusic 
from LoverMusic.plugins import ALL_MODULES
from LoverMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("LoverMusic").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("LoverMusic").warning(
            "Spotify Client Id & Secret not added, Chutiya Saala ek itni simple cheej nahi laa paaya."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("LoverMusic.plugins" + all_module)
    LOGGER("LoverMusic.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Anon.start()
    try:
        await Anon.stream_call(
            "https://telegra.ph/file/de3464aa7d6bfafdd2dc3.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("LoverMusic").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Anon.decorators()
    LOGGER("LoverMusic").info("Music Bot Started Successfully, Now Gib your girlfriend chumt to @shubhamsah1")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("LoverMusic").info("Stopping Music Bot, Bhakk Bhosdike (Gaand Maraa Tu)")
