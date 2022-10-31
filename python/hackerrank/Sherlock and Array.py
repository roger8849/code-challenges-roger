'''
Sherlock and Array
https://www.hackerrank.com/challenges/sherlock-and-array/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    leftSum, rightSum = 0, sum(arr)-arr[0]
    
    # Base case the arr contains only 1 element
    if leftSum == rightSum:
        return 'YES'
    
    n = len(arr)
    # iterate over arr.
    for i in range(1, n):
        leftSum += arr[i-1]
        rightSum -= arr[i]
        if leftSum == rightSum:
            return 'YES'
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
