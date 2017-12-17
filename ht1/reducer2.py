#!/usr/bin/env python
# coding=utf-8

import sys

currentKey = ""
currentCount = 0
currentPtSum = 0
currentEventFileSet = set()

for line in sys.stdin:
    antiNucleus, value = line.split('\t')
    eventFile, Pt = value.split(',')
    Pt = float(Pt)
    
    if currentKey == "":
        currentKey = antiNucleus

    if currentKey != antiNucleus:
        avgPt = currentPtSum / currentCount
        print('%s\t%s\t%s' % (currentKey, str(len(currentEventFileSet)), avgPt))
        currentCount = 0
        currentPtSum = 0
        currentKey = antiNucleus
        currentEventFileSet = set()

    currentCount += 1
    currentPtSum += Pt
    currentEventFileSet.add(eventFile)

avgPt = currentPtSum / currentCount
print('%s\t%s\t%s' % (currentKey, currentCount, avgPt))
