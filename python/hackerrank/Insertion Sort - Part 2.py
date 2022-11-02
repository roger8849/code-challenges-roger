'''
Insertion Sort - Part 2
https://www.hackerrank.com/challenges/insertionsort2/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            right = i + 1
            while right > 0 and arr[right] < arr[right-1]:
                arr[right], arr[right-1] = arr[right-1], arr[right]
                right -= 1
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

    '''
    STDIN           Function
    -----           --------
    6               n = 6
    1 4 3 5 6 2     arr = [1, 4, 3, 5, 6, 2]
    '''
