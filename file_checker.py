#!/usr/bin/python2

import sys

DEFAULT_MAX_LINE_LENGTH = 80 # Including end-of-line character.
DEFAULT_SPACES_PER_TAB = 2
PYTHON_SPACES_PER_TAB = 4

def CheckIndentation(filename,
                     spaces_per_tab=DEFAULT_SPACES_PER_TAB,
                     replace_tabs=False):
    line_num = 0
    lines_with_tabs = {}
    tab_replacement = ''
    for i in range(spaces_per_tab):
        tab_replacement += ' '
    f = open(filename, 'rw')
    lines = f.readlines()
    for line in lines:
        line_num += 1
        if line.contains('\t'):
            lines_with_tabs[line_num] = line
            line = line.replace('\t', tab_replacement)
        if replace_tabs:
            f.write(line)
    f.close()

    return lines_with_tabs

def CheckLineLengths(filename, max_length=DEFAULT_MAX_LINE_LENGTH):
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

    return lines_exceeding_max_length

def main():
    if len(sys.argv) == 1:
        print "Enter filename/directory: "
        inputString =
    else:
        inputList = sys.argv[1:]

    CheckLineLengths(sys.argv[1])

if __name__ == "__main__":
    main()
