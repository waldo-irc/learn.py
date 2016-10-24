#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sopel.module, from sopel.module import example, import collections, import sys, import time, from sopel.tools import iteritems, import sopel.loader, import sopel.module, import subprocess, import re, import json, import random, string

reload(sys)  
sys.setdefaultencoding('utf8')

@sopel.module.commands('bookie')
@example('!bookie command insert stuff here')
def bookie(bot, trigger):
    if not trigger.group(3) or not trigger.group(4) or not trigger.admin:
        bot.say('Usage is !bookie command command goes here')
        bot.say('Must be bot admin to run.')
        exit(0)

    ##Here we check if the dictionary exists and has something in it.  If not, we create an empty dictionary.#######
    try:
        f = open('/home/sopel/.sopel/modules/dictionary', 'r')
        commands = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError):
        commands = {}
 
    symbol = "~`!@#$%^&*()_-+={}[]:>;\"',</?*-+"
    commandexist = "abuse save quit msg part me join set mode unquiet topic kickban kick tmask showmask quiet unban ban announce py wa c settz settimeformat getchanneltz t gettz setchanneltimeformat gettimeformat setchanneltz getchanneltimeformat blocks useserviceauth choose d help iplookup console lmgtfy t0w3ntum deop op rand redditor setsafeforwork getsafeforwork in at safety duck suggest search seen ssh tell tld uptime waldo website w xkcd zncadd"
    arg1x = trigger.group(2).split(" ",1)[1]
    arg1 = arg1x.encode("utf-8")
    arg2x = trigger.group(3)
    arg2 = arg2x.encode("utf-8")
    name = "bookiecmds"

    for i in arg2:
        if i in symbol:
            bot.say("Illegal characters detected.")
            exit(0)

    if u'%s' % arg2.lower() in commands or arg2.lower() == 'bookie' or arg2.lower() == 'unbookie' or arg2.lower() == 'rebookie' or arg2.lower() in commandexist:
        bot.say("Command already exists.") 
        exit(0)

    bot.say("Inserting %s into %s command." % (arg1,arg2))

    def randomword(length):
        return ''.join(random.choice(string.lowercase) for i in range(length))
    funcnum = randomword(6)

    commands[arg2.lower()] = []
    commands[arg2.lower()].append(arg1)
    commands[arg2.lower()].append(funcnum)
    
#    bot.say("%s" % commands)

    with open("/home/sopel/.sopel/modules/bookiecmds.py", 'a') as handle:
        handle.writelines('\n')
        handle.writelines("@sopel.module.commands(u'{0}')".format(arg2.lower()))
        handle.writelines('\n')
        handle.writelines("def func%ssc(bot, trigger):" % funcnum)
        handle.writelines('\n')
        handle.writelines("    bot.say(\"%s\" % commands[u\"{0}\"][0])".format(arg2.lower()))
        handle.writelines('\n')
        f = open('/home/sopel/.sopel/modules/dictionary', 'w')
        f.write(json.dumps(commands))
        f.close()

    ########This is code borrowed from reload.py to reload the module after adding the lines.#########
    old_module = sys.modules[name]

    old_callables = {}
    for obj_name, obj in iteritems(vars(old_module)):
        bot.unregister(obj)

    # Also remove all references to sopel callables from top level of the
    # module, so that they will not get loaded again if reloading the
    # module does not override them.
    for obj_name in old_callables.keys():
        delattr(old_module, obj_name)

    # Also delete the setup function
    if hasattr(old_module, "setup"):
        delattr(old_module, "setup")

    modules = sopel.loader.enumerate_modules(bot.config)
    path, type_ = modules[name]
    load_module(bot, name, path, type_)


def load_module(bot, name, path, type_):
    module, mtime = sopel.loader.load_module(name, path, type_)
    relevant_parts = sopel.loader.clean_module(module, bot.config)

    bot.register(*relevant_parts)

    # TODO sys.modules[name] = module
    if hasattr(module, 'setup'):
        module.setup(bot)

    modified = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(mtime))

    #bot.reply('%r (version: %s)' % (module, modified))
    ######End Reload.py Code###########################

    return bot.say('Done')




@sopel.module.commands('rebookie')
@example('!rebookie command insert stuff here')
def rebookie(bot, trigger):
    if not trigger.group(3) or not trigger.group(4) or not trigger.admin:
        bot.say('Usage is !rebookie command command goes here')
        bot.say('Must be bot admin to run.')
        exit(0)

    ##Here we check if the dictionary exists and has something in it.  If not, we create an empty dictionary.#######
    try:
        f = open('/home/sopel/.sopel/modules/dictionary', 'r')
        commands = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError):
        commands = {}

    name = "bookiecmds"
    arg1 = trigger.group(2).split(" ",1)[1]
    arg2 = trigger.group(3)

    bot.say("Changing %s value to %s." % (arg2,arg1))

    if arg2.lower() not in commands:
        bot.say("Command doesn't exist to rebookie.")
        exit(0)

    funcnum = commands[arg2.lower()][1]
    commands[arg2.lower()] = []
    commands[arg2.lower()].append(arg1)
    commands[arg2.lower()].append(funcnum)

    f = open('/home/sopel/.sopel/modules/dictionary', 'w')
    f.write(json.dumps(commands))
    f.close()

    ########This is code borrowed from reload.py to reload the module after adding the lines.#########
    old_module = sys.modules[name]

    old_callables = {}
    for obj_name, obj in iteritems(vars(old_module)):
        bot.unregister(obj)

    # Also remove all references to sopel callables from top level of the
    # module, so that they will not get loaded again if reloading the
    # module does not override them.
    for obj_name in old_callables.keys():
        delattr(old_module, obj_name)

    # Also delete the setup function
    if hasattr(old_module, "setup"):
        delattr(old_module, "setup")

    modules = sopel.loader.enumerate_modules(bot.config)
    path, type_ = modules[name]
    load_module(bot, name, path, type_)


def load_module(bot, name, path, type_):
    module, mtime = sopel.loader.load_module(name, path, type_)
    relevant_parts = sopel.loader.clean_module(module, bot.config)
 
    bot.register(*relevant_parts)

    # TODO sys.modules[name] = module
    if hasattr(module, 'setup'):
        module.setup(bot)

    modified = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(mtime))

    #bot.reply('%r (version: %s)' % (module, modified))
    ######End Reload.py Code###########################

    return bot.say('Done')   



@sopel.module.commands('bookielist')
@example('!bookielist')
def bookielist(bot, trigger):
    if not trigger.admin:
        bot.say('Must be bot admin to run.')
        exit(0)

    ##Here we check if the dictionary exists and has something in it.  If not, we create an empty dictionary.#######
    try:
        f = open('/home/sopel/.sopel/modules/dictionary', 'r')
        commands = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError):
        commands = {}

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
        bot.msg(trigger.nick,color.BOLD + "Command %s " % x + color.END + '"%s"'  % key.upper())
        x+=1


@sopel.module.commands('unbookie')
@example('!unbookie command')
def unbookie(bot, trigger):
    if not trigger.group(3) or not trigger.admin:
        bot.say('Usage is !unbookie command')
        bot.say('Must be bot admin to run.')
        exit(0)
    
    ##Here we check if the dictionary exists and has something in it.  If not, we create an empty dictionary.#######
    try:
        f = open('/home/sopel/.sopel/modules/dictionary', 'r')
        commands = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError):
        commands = {}

    key = trigger.group(3)
    name = "bookiecmds"

    bot.say("Removing %s command." % (key.lower()))

    if key.lower() not in commands:
        bot.say("Command doesn't exist to unbookie.")
        exit(0)
        
    funcnum = commands[key.lower()][1]
    lookupcmd = "@sopel.module.commands(u'%s')" % key.lower()
    lookupfunc = 'def func%ssc(bot, trigger):' % funcnum

    fileopen = open("/home/sopel/.sopel/modules/bookiecmds.py", 'r')

    with open('/home/sopel/.sopel/modules/bookie.py0', 'w') as myFile:
        for line in fileopen:
            #if lookupcmd not in line or lookupfunc not in line or ("bot.say" not in line and 'commands["{0}"]'.format(key.lower()) not in line):            
            if lookupcmd not in "%s" % line:
                #bot.say('found at line: %s' % num)       
                myFile.write(u'%s' % line)

    fileopen.close()

    fileopen = open('/home/sopel/.sopel/modules/bookie.py0', 'r')

    with open('/home/sopel/.sopel/modules/bookie.py1', 'w') as myFile:
        for line in fileopen:
            #if lookupcmd not in line or lookupfunc not in line or ("bot.say" not in line and 'commands["{0}"]'.format(key.lower()) not in line):            
            if lookupfunc not in line:
                myFile.write(line)

    fileopen.close()

    fileopen = open('/home/sopel/.sopel/modules/bookie.py1', 'r')

    with open('/home/sopel/.sopel/modules/bookie.py2', 'w') as myFile:
        for line in fileopen:
            #if lookupcmd not in line or lookupfunc not in line or ("bot.say" not in line and 'commands["{0}"]'.format(key.lower()) not in line):            
             if 'commands[u"{0}"]'.format(key.lower()) not in line:
                #bot.say('found at line: %s' % num)       
                myFile.write(line)

    fileopen.close()

    subprocess.check_output(['bash','-c', 'cp /home/sopel/.sopel/modules/bookie.py2 /home/sopel/.sopel/modules/bookiecmds.py'])

    del commands["%s" % key.lower()]
    f = open('/home/sopel/.sopel/modules/dictionary', 'w')
    f.write(json.dumps(commands))
    f.close()

    bot.say('Reloading')

    bot.say('Done')

    subprocess.check_output(['bash','-c', 'sopel --quit && sopel -d --quiet'])


lastSpam = {}

@sopel.module.rule('!(.*)bookie(.*)')
def spam(bot, trigger):
    if trigger.nick not in lastSpam:
        lastSpam[trigger.nick] = []
        
    if not trigger.owner:
        lastSpam[trigger.nick].append(trigger.time)

    if len(lastSpam[trigger.nick]) >= 3:
        firstSpam = lastSpam[trigger.nick].pop(0)
        if (trigger.time - firstSpam).seconds <= 10:
            bot.say("Don't abuse the privelege, bot will ignore you for 10 seconds.")
            bot.msg("chanserv", "quiet ##YOURCHANNEL %s" % trigger.nick)
            time.sleep(10)
            bot.msg("chanserv", "unquiet ##YOURCHANNEL %s" % trigger.nick)
