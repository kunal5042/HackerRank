#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

'''
O(n) Time | O(1) Space: where n is the length of the input strings
'''
def matchingStrings(strings, queries):
    result = [0 for query in queries]
    
    (string_frequency, idx1) = ({}, 0)
    
    while idx1 < len(strings):
        string_frequency[strings[idx1]] = string_frequency.get(strings[idx1], 0) + 1
        idx1 += 1
    
    for idx, query in enumerate(queries):
        result[idx] = string_frequency.get(query, 0)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
    
# Kunal Wadhwa
# 6621 1445 5286