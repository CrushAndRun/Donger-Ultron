#!/usr/bin/env python3
import json
import random
helptext = "Outputs a random yomomma phrase."

yomommalist = json.load(open("wisdom/yomomma.json"))
def doit(irc, target, source):
  irc.message(target, random.choice(yomommalist))
