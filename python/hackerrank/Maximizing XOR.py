'''
Maximizing XOR
https://www.hackerrank.com/challenges/maximizing-xor/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
    # Write your code here
    maxNum = -sys.maxsize
    for i in range(l, r+1):
        for j in range(i, r+1):
            maxNum = max(maxNum, i^j)
    return maxNum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
