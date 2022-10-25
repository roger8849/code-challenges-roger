'''
Weighted Uniform Strings
https://www.hackerrank.com/challenges/weighted-uniform-string/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    n = len(s)
    contigousSubsVals = set()
    charSum = ord(s[0]) - ord('a') + 1
    contigousSubsVals.add(charSum)
    for i in range(1, n):
        val = ord(s[i]) - ord('a') + 1
        charSum = charSum + val if s[i] == s[i-1] else val
        contigousSubsVals.add(charSum)
    print(contigousSubsVals)
    res = ['Yes' if q in contigousSubsVals else 'No' for q in queries]
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
