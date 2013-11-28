#!/usr/bin/env python
import random
import yaml
import string
import sys
import os

root = os.path.dirname(os.path.realpath(__file__))
names_file = root + '/nicks.yaml'
char_limit = 32

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
   
def makenames(filename, count=1, limit=float('inf')):
    f = open(filename)
    d = yaml.load(f)
    i = 0
    while i < count:
        nick = randline(d['nicks'])
        phrase = substitute(nick, d)
        if len(phrase) <= limit:
            print phrase
            i += 1

if __name__ == '__main__':
    try:
        count = int(sys.argv[1])
    except:
        count = 1
    makenames(names_file, count, char_limit)
