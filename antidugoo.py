"""
Custom Willie module to bother people who call me a nickname I've repeatedly told them not to use.
"""

import willie.module as module
from random import choice

STRINGS = [
    "Listen to dgw when he tells you not to call him that, %s!",
    "dgw keeps telling you not to call him that, %s.",
    "How many times does dgw have to tell you not to use that name, %s?",
    "Trying to get on dgw's bad side, %s?",
    "Watch out, %s, or dgw will report you to network staff for harassment. :P"
]


@module.rule('.*d(oo|u)gg?oo.*')
@module.require_chanmsg
def antidugoo(bot, trigger):
    if trigger.nick == 'dgw':
        return
    bot.say(choice(STRINGS) % trigger.nick)
