#!/usr/bin/env python
"""reducer.py"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    word_counts = []

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            word_counts.append((current_word, total_count))
        except ValueError:
            # count was not a number, so silently discard this item
            pass

    # sort by count descending and take top 3
    top_3 = sorted(word_counts, key=itemgetter(1), reverse=True)[:3]

    for word, count in top_3:
        print("%s%s%d" % (word, separator, count))

if __name__ == "__main__":
    main()