#!/usr/bin/env python
# coding=utf-8

import sys
from decimal import *

currentKey = ""
agg = []

for line in sys.stdin:
    antiNucleus, prodTime = line.split('\t')
    prodTime = Decimal(prodTime)

    if currentKey == "":
        currentKey = antiNucleus

    if currentKey != antiNucleus:
        agg = sorted(agg)
        lo, hi = agg[int(0.05 * len(agg))], agg[int(0.95 * len(agg))]
        print('%s\t%s\t%s' % (currentKey, lo, hi))

        currentKey = antiNucleus
        agg = []

    agg.append(prodTime)

agg = sorted(agg)
lo, hi = agg[int(0.05 * len(agg))], agg[int(0.95 * len(agg))]
print('%s\t%s\t%s' % (currentKey, lo, hi))
