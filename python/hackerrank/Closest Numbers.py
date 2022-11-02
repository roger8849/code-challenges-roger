'''
Closest Numbers
https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    minDiff = sys.maxsize
    arr.sort()
    res = list()
    for i in range(1, len(arr)):
        a, b = arr[i], arr[i-1]
        if a - b == minDiff:
            res.append(b)
            res.append(a)
        elif a - b < minDiff:
            res = list()
            res.append(b)
            res.append(a)
            minDiff = a - b
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
