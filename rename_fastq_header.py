#!/usr/bin/python

import sys

line_num = 0
for line in iter(sys.stdin.readline, ""):
    line_num += 1
    print line,
