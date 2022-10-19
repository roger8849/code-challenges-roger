'''
Intro to Tutorial Challenges
https://www.hackerrank.com/challenges/tutorial-intro/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'introTutorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr
#
def binarySearch(V, arr):
    start, end = 0, len(arr)-1
    
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == V:
            return mid
        elif arr[mid] < V:
            start = mid + 1
        else:
            end = mid - 1
    return -1
    
def introTutorial(V, arr):
    # Write your code here
    return binarySearch(V, arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
