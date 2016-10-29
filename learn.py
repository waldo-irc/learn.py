#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sopel.module
from sopel.module import example, priority
import collections
import sys
import time
from sopel.tools import iteritems
import sopel.loader
import sopel.module
import subprocess
import re
import json
import random, string
import datetime
from dateutil.parser import parse as parse_date
import calendar
from sopel.formatting import bold
import textwrap
from os.path import expanduser
import os

reload(sys)
sys.setdefaultencoding('utf8')

#######Commands start here################
@sopel.module.commands('bookie')
@example('!bookie command insert stuff here')
def bookie(bot, trigger):
    if not trigger.group(3) or not trigger.group(4):
        bot.say('Usage is !bookie command command goes here')
        exit(0)

    ##Here we check if the dictionary exists and has something in it.  If not, we create an empty dictionary.#######
    try:
        f = open(os.path.join(os.path.expanduser('~'),'.sopel/learn_cmds'), 'r')
        commands = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError, AttributeError, IOError):
        commands = {}
    ##Here we load anyone that has already made a command and must wait##
    try:
        f = open(os.path.join(os.path.expanduser('~'),'.sopel/learn_bl'), 'r')
        lastRule = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError, AttributeError, IOError):
        lastRule = {}

    name_length = max(6, max(len(k) for k in bot.command_groups.keys()))
    currenttime = calendar.timegm(trigger.time.timetuple())
    today = datetime.datetime.today()
    symbol = "~`!@#$%^&*()_-+={}[]:>;\"',</?*-+\\\\\\"
    arg1x = trigger.group(2).split(" ",1)[1]
    arg1 = arg1x.encode("utf-8")
    arg2x = trigger.group(3)
    arg2 = arg2x.encode("utf-8")
    count = 0
    y = 0

    if trigger.is_privmsg:
        bot.msg("waldo", u'%s using !bookie %s' % (trigger.nick,arg1))

    for key, value in commands.iteritems():
        y+=1

    if y >= 50:
        bot.say("Command limit reached (50 commands max). %s Commands currently." % y)
        exit(0)

    for i in arg2:
        count+=1
        if i in symbol:
            bot.say("Illegal characters detected in command name.")
            exit(0)

    if count > 15:
        bot.say("Command name has a 15 character limit.")
        exit(0)

    for category, cmds in collections.OrderedDict(sorted(bot.command_groups.items())).items():
        for line in cmds:
            if line.lower() == arg2.lower():
                bot.say('%s is already a Sopel command.' % line)
                exit(0)

    if u'%s' % arg2.lower() in commands or arg2.lower() == 'bookie' or arg2.lower() == 'unbookie' or arg2.lower() == 'rebookie' or arg2.lower() == 'bookielist' or arg2.lower() == 'mybookielist':
        bot.say("Command already exists in Sopel learn.")
        exit(0)

    if u'%s' % trigger.nick.lower() in lastRule and not trigger.admin:
        oldtime = datetime.datetime.utcfromtimestamp(lastRule[u'%s' % trigger.nick.lower()][0])
        newtime = datetime.datetime.utcnow()
        if ( newtime - oldtime ) < datetime.timedelta(hours=24):
            bot.say("Must wait 24 hours before creating a new command.")
            exit(0)
        else:
            del lastRule[u'%s' % trigger.nick.lower()]

    if u'%s' % trigger.nick.lower() not in lastRule and not trigger.admin:
        lastRule[u'%s' % trigger.nick.lower()] = []
        lastRule[u'%s' % trigger.nick.lower()].append(currenttime)
        f = open(os.path.join(os.path.expanduser('~'),'.sopel/learn_bl'), 'w+')
        f.write(json.dumps(lastRule))
        f.close()

    bot.say("Inserting %s into %s command." % (arg1,arg2))

    commands[arg2.lower()] = []
    commands[arg2.lower()].append(arg1)
    commands[arg2.lower()].append(trigger.nick.lower())

    f = open(os.path.join(os.path.expanduser('~'),'.sopel/learn_cmds'), 'w')
    f.write(json.dumps(commands))
    f.close()

    return bot.say('Done')


@sopel.module.commands('rebookie')
@example('!rebookie command insert stuff here')
def rebookie(bot, trigger):
    if not trigger.group(3) or not trigger.group(4):
        bot.say('Usage is !rebookie command command goes here')
        exit(0)

    ##Here we check if the dictionary exists and has something in it.  If not, we create an empty dictionary.#######
    try:
        f = open(os.path.join(os.path.expanduser('~'),'.sopel/learn_cmds'), 'r')
        commands = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError, IOError):
        commands = {}

    arg1 = trigger.group(2).split(" ",1)[1]
    arg2 = trigger.group(3).encode("utf-8")

    if trigger.is_privmsg:
        bot.msg("waldo", u'%s using !rebookie %s' % (trigger.nick,arg1))

    bot.say("Changing %s value to %s." % (arg2,arg1))

    if u"%s" % arg2.lower() not in commands:
        bot.say("Command doesn't exist to rebookie.")
        exit(0)

    if trigger.nick.lower() in commands[u'%s' % arg2.lower()][1] or trigger.admin:
        creator = commands[u'%s' % arg2.lower()][1]
        commands[u'%s' % arg2.lower()] = []
        commands[u'%s' % arg2.lower()].append(arg1)
        commands[u'%s' % arg2.lower()].append(creator)

        f = open(os.path.join(os.path.expanduser('~'),'.sopel/learn_cmds'), 'w')
        f.write(json.dumps(commands))
        f.close()

        return bot.say('Done')
    else:
        bot.say("Must be Command Creator or admin to change.")


@sopel.module.commands('bookielist')
@priority('low')
@example('!bookielist')
def bookielist(bot, trigger):
    ##Here we check if the dictionary exists and has something in it.  If not, we create an empty dictionary.#######
    try:
        f = open(os.path.join(os.path.expanduser('~'),'.sopel/learn_cmds'), 'r')
        commands = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError, IOError):
        commands = {}

    if trigger.is_privmsg:
        bot.msg("waldo", u'%s using !bookielist' % trigger.nick)

    bot.say("PM'ing you a list of created commands.")

    x = 1

    class color:
       PURPLE = '\033[95m'
       CYAN = '\033[96m'
       DARKCYAN = '\033[36m'
       BLUE = '\033[94m'
       GREEN = '\033[92m'
       YELLOW = '\033[93m'
       RED = '\033[91m'
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
       END = '\033[0m'

    bot.msg(trigger.nick,color.BOLD + "###LISTING COMMANDS###" + color.END)
    for key, value in commands.iteritems():
        if commands[key][1] == trigger.nick:
            bot.msg(trigger.nick,color.BOLD + "Command %s " % x + color.END + '"%s"'  % key.upper() + " *(You created this)")
            x+=1
        elif trigger.admin:
            bot.msg(trigger.nick,color.BOLD + "Command %s " % x + color.END + '"%s"'  % key.upper() + u' *(Made by %s)' % commands[key][1])
            x+=1
        else:
            bot.msg(trigger.nick,color.BOLD + "Command %s " % x + color.END + '"%s"'  % key.upper())
            x+=1

@sopel.module.commands('mybookielist')
@priority('low')
@example('!mybookielist')
def mybookielist(bot, trigger):
    ##Here we check if the dictionary exists and has something in it.  If not, we create an empty dictionary.#######
    try:
        f = open(os.path.join(os.path.expanduser('~'),'.sopel/learn_cmds'), 'r')
        commands = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError, IOError):
        commands = {}

    if trigger.is_privmsg:
        bot.msg("waldo", u'%s using !mybookielist' % trigger.nick)

    bot.say("PM'ing you a list of created commands.")

    x = 1

    class color:
       PURPLE = '\033[95m'
       CYAN = '\033[96m'
       DARKCYAN = '\033[36m'
       BLUE = '\033[94m'
       GREEN = '\033[92m'
       YELLOW = '\033[93m'
       RED = '\033[91m'
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
       END = '\033[0m'

    bot.msg(trigger.nick,color.BOLD + "###LISTING COMMANDS###" + color.END)
    for key, value in commands.iteritems():
        if commands[key][1] == trigger.nick:
            bot.msg(trigger.nick,color.BOLD + "Command %s " % x + color.END + '"%s"'  % key.upper() + " *(You created this)")
            x+=1

@sopel.module.commands('unbookie')
@example('!unbookie command')
def unbookie(bot, trigger):
    if not trigger.group(3):
        bot.say('Usage is !unbookie command')
        exit(0)

    ##Here we check if the dictionary exists and has something in it.  If not, we create an empty dictionary.#######
    try:
        f = open(os.path.join(os.path.expanduser('~'),'.sopel/learn_cmds'), 'r')
        commands = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError, IOError):
        commands = {}

    key = trigger.group(3).encode("utf-8")

    if trigger.is_privmsg:
        bot.msg("waldo", u'%s using !unbookie %s' % (trigger.nick, key))

    bot.say("Removing %s command." % (key.lower()))

    if u'%s' % key.lower() not in commands:
        bot.say("Command doesn't exist to unbookie.")
        exit(0)

    if trigger.nick.lower() in commands[u'%s' % key.lower()][1] or trigger.admin:
        del commands[u'%s' % key.lower()]
        f = open(os.path.join(os.path.expanduser('~'),'.sopel/learn_cmds'), 'w')
        f.write(json.dumps(commands))
        f.close()
        bot.say('Done')
    else:
        bot.say("Must be Command Creator or admin to change.")


##########Custom commands spawn here####################################

@sopel.module.rule('\!(.*)')
@priority('high')
def bookienew(bot, trigger):
    try:
        try:
            f = open(os.path.join(os.path.expanduser('~'),'.sopel/learn_cmds'), 'r')
            commands = json.loads(f.read())
            f.close()
        except (RuntimeError, TypeError, NameError, ValueError, IOError):
            commands = {}

        bot.say("%s" % commands[u"%s" % trigger.group(1).lower()][0])
    except KeyError:
        exit(0)
