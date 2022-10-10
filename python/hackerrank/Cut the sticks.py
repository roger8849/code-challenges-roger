'''
https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    n, res, left = len(arr), list(), 0
    arr = sorted(arr)
    while left < n:
        right = left + 1
        res.append(n-left)
        while right < n and arr[left] == arr[right]:
            right += 1
        else:
            left = right
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    ''''
    TC 1
    6
    5 4 4 2 2 8

    TC 2
    8
    1 2 3 4 3 3 2 1

    TC 2
    10
    1 2 3 4 3 3 2 1 4 4
    
    TC 3
    0
    
    
    '''

    result = cutTheSticks(arr)

    assert result == [6,4,2,1] if arr == [5,4,4,2,2,8] else True
    assert result == [8,6,4,1] if arr == [1, 2, 3, 4, 3, 3, 2, 1] else True
    assert result == [10,8,6,3] if arr == [1, 2, 3, 4, 4, 4, 3, 3, 2, 1] else True
    assert result == [] if arr == [] else True

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
