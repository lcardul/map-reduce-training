# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:09:29 2017

@author: loris
"""

#! /usr/bin/env python
import sys

current_word = None
current_count = 0
word = None

f = open('out-mapper.txt', 'r')
myDict = {}
linenum = 0
for line in f:
    line = line.strip()
    line = line.lower()
    line = line.split()
    linenum += 1
    for word in line:
        word = word.strip()
        word = word.lower()
        if not word in myDict:
            myDict[word] = []
        myDict[word].append(linenum)
print ("Il numero 1 della prima riga non e' da considerarsi")
print ('%-15s %5s  %s' %("Word", 'Count', "Line Numbers"))
#print ('hello %s mimmo %s' %'word,ciccio')
for key in sorted(myDict):
    print ('%-15s %5d: %s' % (key, len(myDict[key]), myDict[key]))
f.close()