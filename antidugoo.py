"""
Custom Willie module to bother people who call me a nickname I've repeatedly told them not to use.
"""

import willie.module as module


@module.rule('.*dugoo.*')
@module.require_chanmsg
def antidugoo(bot, trigger):
    bot.say("Listen to dgw when he tells you not to call him that, %s!" % trigger.nick)
