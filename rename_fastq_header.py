#!/usr/bin/python
# -*- coding utf-8 -*-

import sys

if __name__ == "__main__":
    header_arg = []
    for a in sys.argv[1:]:
        header_arg.append(a)
    line_num = 0
    read_num = 0
    for line in iter(sys.stdin.readline, ""):
        line_num += 1
        if line.startswith('@'):
            read_num += 1
            header = line.rstrip("\n")
            header_new = []
            header_new.append(header)
            header_new.extend(header_arg)
            header_new.append(str(read_num))
            print "_".join(header_new)
        else:
            print line,
