'''
Quicksort 1 - Partition
https://www.hackerrank.com/challenges/quicksort1/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    pivot = arr[0]
    left = 1
    for right in range(1,len(arr)):
        if arr[right] < pivot:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    arr[left-1], arr[0] = arr[0], arr[left-1]
    return arr

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    '''
        STDIN       Function
    -----       --------
    5           arr[] size n =5
    4 5 3 7 2   arr =[4, 5, 3, 7, 2]
    '''
    result = quickSort(arr)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
