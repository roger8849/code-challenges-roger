"""
Beautiful Triplets
https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def searchNum(arr, start, end, k):
    """
    _summary_

    Args:
        arr (_type_): _description_
        start (_type_): _description_
        end (_type_): _description_
        k (_type_): _description_

    Returns:
        _type_: _description_
    """
    while start <= end:
        mid = start + (end -start)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            start = mid + 1
        else :
            end = mid - 1
    return -1
def beautifulTriplets(d, arr):
    # Write your code here
    res = 0
    n = len(arr)
    for i in range(n - 2):
        first, second = arr[i], None
        index = -1
        index = searchNum(arr, i + 1, len(arr)-1, first + d)
        if index == -1 or index == n-1:
            continue
        second = arr[index]
        index = searchNum(arr, index + 1, len(arr)-1, second + d)
        if index == -1:
            continue
        res += 1
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    """
    STDIN           Function
    -----           --------
    7 3             arr[] size n = 7, d = 3
    1 2 4 5 7 8 10  arr = [1, 2, 4, 5, 7, 8, 10]
    op = 3
    """

    result = beautifulTriplets(d, arr)

    assert result == 3 if d == 3 and arr == [1,2,4,5,7,8,10] else True

    # fptr.write(str(result) + '\n')

    # fptr.close()
