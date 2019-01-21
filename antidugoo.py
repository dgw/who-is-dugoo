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
    bot.say(choice(RETORTS) % choice((trigger.nick, steal_letters(trigger.nick))))
    if bot.privileges[trigger.sender][bot.nick] > module.HALFOP:
        bot.write(['KICK', trigger.sender, trigger.nick], "R-E-S-P-E-C-T, find out what it means to me!")


@module.rule('.*butts.*')
@module.require_chanmsg
def butt_kicker(bot, trigger):
    if trigger.nick == 'Slyphoria':
        bot.write(['KICK', trigger.sender, trigger.nick], "WHAT WHAT IN YOUR BUTT?")


@module.rule('.*penis.*')
@module.require_chanmsg
def penisword(bot, trigger):
    if trigger.nick == 'Slyphoria':
        bot.write(['KICK', trigger.sender, trigger.nick], "SLAIN BY THE PENISWORD!")


def steal_letters(name):
    consonant_indices = [idx for idx, c in enumerate(name) if c.lower() in 'bcdfghjklmnpqrstvwxyz']
    vowel_indices = [idx for idx, c in enumerate(name) if c.lower() in 'aeiou']
    if (  consonant_indices and len(consonant_indices) >= 2 and consonant_indices[0] == 0
          and vowel_indices and len(vowel_indices) >= 1  ):
        return '{0}{1}{2}{2}oo'.format(name[consonant_indices[0]], name[vowel_indices[0]], name[consonant_indices[1]])
    return name
