'''
Priyanka and Toys
https://www.hackerrank.com/challenges/priyanka-and-toys/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    # Write your code here
    w.sort()
    containers = 0
    n = len(w)
    left, right = 0 ,0
    while left < n:
        mini = w[left]
        while right < n and w[right] <= mini + 4:
            right += 1
        else:
            containers +=1
            left = right
    return containers

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    # fptr.write(str(result) + '\n')

    # fptr.close()
