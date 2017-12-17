#!/usr/bin/env python
# coding=utf-8

import sys

for line in sys.stdin:
    row = line.split(', ')
    print('%s\t%s' % (row[0], row[10]))
