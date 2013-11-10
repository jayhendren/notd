#!/usr/bin/env python
import random
import yaml
import string
import os

root = os.path.dirname(__file__)
names_file = root + '/nicks.yaml'

def randline(l):
    return l[random.randint(0, len(l)-1)]

def substitute(line, mapping):
    result = line
    formatter = string.Formatter()
    madeSub = True
    while madeSub:
        tmp = ''
        madeSub = False
        for element in formatter.parse(result):
            substr = element[0]
            key = element[1]
            tmp = tmp + substr
            if key:
                tmp = tmp + randline(mapping[key])
                madeSub = True
        result = tmp
    return result
   

if __name__ == '__main__':
    f = open(names_file)
    d = yaml.load(f)
    nick = randline(d['nicks'])
    print substitute(nick, d)
