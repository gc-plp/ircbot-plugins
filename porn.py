import os
import re
import praw
import random
import asyncio
from cloudbot import hook
from datetime import datetime

USER_AGENT = "Image fetcher for Snoonet:#Romania by /u/programatorulupeste"
domains = ['imgur.com', 'gfycat.com', 'redditmedia.com']

class cache_elem:
    last_fetch = None
    links = None
    def __init__(self):
        self.last_fetch = 0
        self.links = []

caches = {}

def refresh_cache(r, el):
    print("Refreshing cache for " + el)
    subreddit = r.subreddit(el)
    caches[el].links.clear()
    for submission in subreddit.top("month"):
        if not submission.is_self:
            for domain in domains:
                if domain in submission.url:
                    caches[el].links.append(submission)
                    break
    caches[el].last_fetch = datetime.utcnow()

def get_links_from_subs(sub):
    data = []
    r = praw.Reddit("irc_bot", user_agent=USER_AGENT)

    now = datetime.utcnow()

    for el in sub:
        if el in caches:
            print("Found cache for " + el)
            el_cache = caches[el]
            # Cache older than 2 hours?
            if (now - el_cache.last_fetch).total_seconds() > 7200:
                refresh_cache(r, el)

            data.extend(el_cache.links)
        else:
            print("Cold cache for " + el)
            caches[el] = cache_elem()
            refresh_cache(r, el)
            data.extend(caches[el].links)
    return data

@asyncio.coroutine
@hook.on_start()
def init():
    data = ""
    with open(os.path.realpath(__file__)) as f:
        data = f.read()

    data = data.replace(" ", "")
    data = data.replace("\n","")
    data = data.replace("\'","")
    data = data.replace("\"","")

    start = "get_links_from_subs" + "(["
    end = "])"

    startpos = 0
    endpos = 0
    while True:
        startpos = data.find(start, startpos)
        endpos = data.find(end, startpos)

        if startpos == -1:
            break

        subs = data[startpos + len(start):endpos].split(",")
        get_links_from_subs(subs)

        startpos += len(start)

@hook.periodic(300, initial_interval=30)
def refresh_porn():
    print("Refreshing...")
    for el in caches:
        fake_list = [el]
        get_links_from_subs(fake_list)

@hook.command()
def roscate(message, text, nick):
    data = get_links_from_subs(['ginger', 'redheads', 'RedheadGifs'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def tatuate(message, text, nick):
    data = get_links_from_subs(['altgonewild'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def nsfwfunny(message, text, nick):
    data = get_links_from_subs(['nsfwfunny'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def craci(message, text, nick):
    data = get_links_from_subs(['thighhighs', 'stockings'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def buci(message, text, nick):
    data = get_links_from_subs(['ass', 'asstastic', 'assinthong', 'pawg'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def tzatze(message, text, nick):
    data = get_links_from_subs(['boobs', 'boobies', 'BiggerThanYouThought'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def fetish(message, text, nick):
    data = get_links_from_subs(['kinky', 'bdsm', 'bondage', 'collared', 'lesdom'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def teen(message, text, nick):
    data = get_links_from_subs(['LegalTeens', 'Just18', 'youngporn', 'barelylegal'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def sloboz(message, text, nick):
    data = get_links_from_subs(['cumsluts', 'GirlsFinishingTheJob'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def anal(message, text, nick):
    data = get_links_from_subs(['anal', 'painal'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def milf(message, text, nick):
    data = get_links_from_subs(['milf'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def amateur(message, text, nick):
    data = get_links_from_subs(['RealGirls', 'Amateur', 'GoneWild'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def traps(message, text, nick):
    data = get_links_from_subs(['Tgirls', 'traps', 'gonewildtrans', 'tgifs'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def aww():
    data = get_links_from_subs(['aww'])

    return random.choice(data).url + " aww..."

@hook.command()
def pisi():
    data = get_links_from_subs(['cats'])

    return random.choice(data).url + " aww..."

@hook.command()
def capre():
    data = get_links_from_subs(['doggy'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def lesbiene():
    data = get_links_from_subs(['dykesgonewild', 'dyke'])

    return random.choice(data).url + " NSFW!"
