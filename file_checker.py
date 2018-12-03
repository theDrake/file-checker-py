#!/usr/bin/python2

import sys
import os
from os import path

_DEFAULT_MAX_LINE_LENGTH = 80

def _check_file(filename, max_line_len, check_line_len, check_tabs):
    fin = open(filename, 'r')
    lines = fin.readlines()
    fin.close()
    line_num = 0
    lines_exceeding_max_length = []
    lines_with_tabs = []
    issue_found = False
    for line in lines:
        line_num += 1
        if check_line_len and len(line) > max_line_len + 1: # exclude \n
            lines_exceeding_max_length.append(line_num)
            issue_found = True
        if check_tabs and line.find('\t') != -1:
            lines_with_tabs.append(line_num)
            issue_found = True
    if issue_found:
        print(filename)
        if check_line_len and len(lines_exceeding_max_length) > 0:
            print("\t" + "Line(s) exceeding " + str(max_line_len) +
                  " characters: \n\t\t" + str(lines_exceeding_max_length))
        if check_tabs and len(lines_with_tabs) > 0:
            print("\t" + "Tab(s) found in the following line(s): \n\t\t" +
                  str(lines_with_tabs))

def _check_dir(dir, max_line_len, check_line_len, check_tabs):
    if dir[-1] != '/':
        dir += '/'
    subdirs = []
    for i in os.listdir(dir):
        if path.isdir(i):
            subdirs.append(i)
        elif path.isfile(dir + i):
            _check_file(dir + i, max_line_len, check_line_len, check_tabs)
    for s in subdirs:
        _check_dir(dir + s, max_line_len, check_line_len, check_tabs)

def main():
    max_line_len = _DEFAULT_MAX_LINE_LENGTH
    check_line_len = True
    check_tabs = True
    input_list = []
    if len(sys.argv) == 1:
        print("Usage: file_checker.py dir [--maxlen=n | --no-len-check | "
              "--no-tab-check]")
    else:
        for arg in sys.argv[1:]:
            if arg[:9] == "--maxlen=":
                max_line_len = int(arg[9:])
            elif arg == "--no-len-check":
                check_line_len = False
            elif arg == "--no-tab-check":
                check_tabs = False
            else:
                input_list.append(arg)
        for i in input_list:
            if path.isdir(i):
                _check_dir(path.abspath(i), max_line_len, check_line_len, check_tabs)
            else:
                print("Invalid input: " + i)

if __name__ == "__main__":
    main()
