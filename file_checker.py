#!/usr/bin/env python3

import sys
import os
from os import path

_USAGE = "file_checker.py target [target2 ...] [--maxlen=n | --no-len-check" + \
         " | --no-tab-check | --check-hidden-files | --check-hidden-dirs]"
_DEFAULT_MAX_LINE_LENGTH = 80

def _check_file(filename, max_line_len, check_line_len, check_tabs):
    print("Checking file: " + filename)
    fin = open(filename, 'r')
    lines = fin.readlines()
    fin.close()
    line_num = 0
    lines_exceeding_max_length = []
    lines_with_tabs = []
    for line in lines:
        line_num += 1
        if check_line_len and len(line) > max_line_len + 1: # exclude '\n'
            lines_exceeding_max_length.append(line_num)
        if check_tabs and line.find('\t') != -1:
            lines_with_tabs.append(line_num)
    if len(lines_exceeding_max_length) > 0:
        print("\t" + "Line(s) exceeding " + str(max_line_len) +
              " characters:\t" + str(lines_exceeding_max_length))
    if len(lines_with_tabs) > 0:
        print("\t" + "Tab(s) found in the following line(s):\t" +
              str(lines_with_tabs))

def _check_dir(dir, max_line_len, check_line_len, check_tabs, check_hidden_dirs,
               check_hidden_files):
    if dir[-1] != '/':
        dir += '/'
    print("Scanning dir: " + dir)
    subdirs = []
    for i in os.listdir(dir):
        if path.isdir(dir + i):
            if i[0] != '.' or check_hidden_dirs:
                subdirs.append(i)
            else:
                print("Ignoring dir: " + i)
        elif path.isfile(dir + i):
            if i[0] != '.' or check_hidden_files:
                _check_file(dir + i, max_line_len, check_line_len, check_tabs)
            else:
                print("Ignoring file: " + i)
    for s in subdirs:
        _check_dir(dir + s, max_line_len, check_line_len, check_tabs,
                   check_hidden_dirs, check_hidden_files)

def main():
    max_line_len = _DEFAULT_MAX_LINE_LENGTH
    check_line_len = True
    check_tabs = True
    check_hidden_dirs = False
    check_hidden_files = False
    input_list = []
    if len(sys.argv) == 1:
        print("Usage: " + _USAGE)
    else:
        for arg in sys.argv[1:]:
            if arg[:9] == "--maxlen=":
                max_line_len = int(arg[9:])
            elif arg == "--no-len-check":
                check_line_len = False
            elif arg == "--no-tab-check":
                check_tabs = False
            elif arg == "--check-hidden-dirs":
                check_hidden_dirs = True
            elif arg == "--check-hidden-files":
                check_hidden_files = True
            else:
                input_list.append(arg)
        for i in input_list:
            if path.isdir(i):
                _check_dir(path.abspath(i), max_line_len, check_line_len,
                           check_tabs, check_hidden_dirs, check_hidden_files)
            elif path.isfile(i):
                _check_file(path.abspath(i), max_line_len, check_line_len,
                            check_tabs)
            else:
                print("Invalid input: " + i)

if __name__ == "__main__":
    main()
