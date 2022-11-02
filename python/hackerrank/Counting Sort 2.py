'''
Counting Sort 2
https://www.hackerrank.com/challenges/countingsort2/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    #  Write your code here
    res = [0]*100
    for num in arr:
        res[num] += 1
    return [i for i in range(len(res)) for j in range(res[i])]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()