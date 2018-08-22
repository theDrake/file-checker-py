#!/usr/bin/python2

import sys, os, os.path

DEFAULT_MAX_LINE_LENGTH = 80
DEFAULT_SPACES_PER_TAB = 2
PYTHON_SPACES_PER_TAB = 4

def CheckIndentation(filename, spaces_per_tab=DEFAULT_SPACES_PER_TAB,
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
    line_num = 0
    lines_exceeding_max_length = {}
    for line in lines:
        line_num += 1
        if line.length() > max_length:
            lines_exceeding_max_length[line_num] = line
    print 'File "' + filename + '" contains ' + \
          len(lines_exceeding_max_length) + ' lines exceeding ' + \
          max_length + ' characters.'

    return lines_exceeding_max_length

def main():
    os.mkdir('./file_checker_backups')
    input_list = []
    if len(sys.argv) == 1:
        input_list.append(raw_input("Enter filename/directory: "))
    else:
        input_list.extend(sys.argv[1:])

if __name__ == "__main__":
    main()
