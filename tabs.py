#!/usr/bin/env python

def ReplaceTabsWithFourSpaces(filename):
    tab_count = 0
    f = open(filename, 'rw')
    lines = f.readlines()
    for line in lines:
        if line.contains('\t'):
            tab_count += 1
    f.close()

def main():
    

if __name__ == "__main__":
    main()
