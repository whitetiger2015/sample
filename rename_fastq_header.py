#!/usr/bin/python
# -*- coding utf-8 -*-

import sys

if __name__ == "__main__":
    line_num = 0
    read_num = 0
    for line in iter(sys.stdin.readline, ""):
        line_num += 1
        if line.startswith('@'):
            read_num += 1
            header = line.rstrip("\n")
            header = header + '_' + str(read_num)
            print header
        else:
            print line,
