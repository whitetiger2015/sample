#!/usr/bin/python
# -*- coding utf-8 -*-

import sys

if __name__ == "__main__":
    line_num = 0
    for line in iter(sys.stdin.readline, ""):
        line_num += 1
        print line,
