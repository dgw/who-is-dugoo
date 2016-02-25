"""
Custom Sopel module to bother people who call me a nickname I've repeatedly told them not to use.
"""

import sopel.module as module
from random import choice

RETORTS = [
    "Listen to dgw when he tells you not to call him that, %s!",
    "dgw keeps telling you not to call him that, %s.",
    "How many times does dgw have to tell you not to use that name, %s?",
    "Trying to get on dgw's bad side, %s?",
    "Really, %s?",
    "There's a time and a place for calling dgw that, %s. Actually, there isn't. Ever.",
    "You know not to call dgw that, %s. How can you live with the guilt?"
]


@module.rule('.*d(oo|u)gg?oo.*')
@module.require_chanmsg
def antidugoo(bot, trigger):
    if trigger.nick == 'dgw' or trigger.nick == bot.nick:
        return
    bot.say(choice(RETORTS) % trigger.nick)
    if bot.privileges[trigger.sender][bot.nick] > module.HALFOP:
        bot.write(['KICK', trigger.sender, trigger.nick], "R-E-S-P-E-C-T, find out what it means to me!")
