#!/usr/bin/env python

def CheckLineLengths(filename, max_length=80):
    num_lines_exceeding_max_length = 0
    fin = open(filename, 'r')
    lines = fin.readlines()
    for line in lines:
        if line.length() > max_length:
            num_lines_exceeding_max_length += 1
    fin.close()
    print 'File "' + filename + '" contains ' + \
          num_lines_exceeding_max_length + ' lines exceeding ' + max_length + \
          ' characters.'
    return num_lines_exceeding_max_length

def main():
    CheckLineLengths(filename)

if __name__ == "__main__":
    main()
