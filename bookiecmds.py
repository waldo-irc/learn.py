#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sopel.module
from sopel.module import example
import collections
import sys
import time
from sopel.tools import iteritems
import sopel.loader
import sopel.module
import subprocess
import re
import json

##Here we check if the dictionary exists and has something in it.  If not, we create an empty dictionary.#######
try:
    f = open('/home/sopel/.sopel/modules/dictionary', 'r')
    commands = json.loads(f.read())
    f.close()
except (RuntimeError, TypeError, NameError, ValueError):
    commands = {}

##Custom Commands goes here
