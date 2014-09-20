#!/usr/bin/python

import trans
import sys

def main():
    for i in sys.argv[1:]:
        with open(i, 'r') as f:
            print trans.trans(f.read())

if __name__ == '__main__':
    main()
