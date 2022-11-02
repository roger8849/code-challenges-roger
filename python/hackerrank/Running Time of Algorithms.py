'''
Running Time of Algorithms
https://www.hackerrank.com/challenges/runningtime/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
    shifts = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            right = i + 1
            while right > 0 and arr[right] < arr[right-1]:
                shifts += 1
                arr[right], arr[right-1] = arr[right-1], arr[right]
                right -= 1
        print(*arr)
    return shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
