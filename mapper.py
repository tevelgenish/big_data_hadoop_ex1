#!/usr/bin/env python
"""mapper.py"""

import sys

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            # strip trailing commas/dots and convert to lowercase
            cleaned_word = word.rstrip('.,').lower()
            if cleaned_word:
                print('%s%s%d' % (cleaned_word, separator, 1))

if __name__ == "__main__":
    main()