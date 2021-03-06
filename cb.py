import asyncio
import os
import cloudbot
from cloudbot import hook
from cleverwrap import CleverWrap

@hook.on_start()
def get_key(bot):
    global api_key, cb
    api_key = bot.config.get("api_keys", {}).get("cleverbot", None)
    cb = CleverWrap(api_key)

@hook.command
def coaie(text):
    return cb.say(text)
