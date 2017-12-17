#!/usr/bin/env python
# coding=utf-8

import sys
from decimal import *

quantiles = {}
for line in open('quantiles.txt', 'r'):
    antiNucleus, lo, hi = line.split('\t')
    quantiles[antiNucleus] = (Decimal(lo), Decimal(hi))

for line in sys.stdin:
    row = line.split(', ')
    antiNucleus = row[0]
    prodTime = Decimal(row[10])
    if prodTime >= quantiles[antiNucleus][0] and prodTime <= quantiles[antiNucleus][1]:
        print('%s\t%s,%s' % (row[0], row[1], row[11]))
