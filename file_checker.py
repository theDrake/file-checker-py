#!/usr/bin/env python

import sys


def ReplaceTabsWithSpaces(filename, spaces_per_tab):
    tab_count = 0
    f = open(filename, 'rw')
    lines = f.readlines()
    f.close()
    for line in lines:
        if line.contains('\t'):
            tab_count += 1


def CheckLineLengths(filename, max_length=80):
    fin = open(filename, 'r')
    lines = fin.readlines()
    fin.close()
    lines_exceeding_max_length = []
    for line in lines:
        if line.length() > max_length:
            num_lines_exceeding_max_length += 1
    print 'File "' + filename + '" contains ' + \
          num_lines_exceeding_max_length + ' lines exceeding ' + max_length + \
          ' characters.'
    return num_lines_exceeding_max_length


def main():
    for len(sys.argv) > 1:
        CheckLineLengths(sys.argv[1])


if __name__ == "__main__":
    main()
