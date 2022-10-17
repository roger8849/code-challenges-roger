'''
Minimum Distances
https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    res = None

    for left in range(len(a)-1):
        for right in range(left+1, len(a)):
            if a[left] == a[right]:
                res = right - left if not res or (right - left < res) else res

    return -1 if not res else res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
