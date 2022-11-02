'''
Largest Permutation
https://www.hackerrank.com/challenges/largest-permutation/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    # Write your code here
    dict_ = {}
    for i, a in enumerate(arr):
        dict_[a] = i
    cnt = 0
    n = len(arr)
    for i in range(n):
        if cnt == k:
            break
        v = arr[i]
        if v < n - i:
            arr[i], arr[dict_[n-i]] = arr[dict_[n-i]], arr[i]
            dict_[v], dict_[n-i] = dict_[n-i], dict_[v]
            cnt += 1
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
