'''
Beautiful Binary String
https://www.hackerrank.com/challenges/beautiful-binary-string/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    # Write your code here
    ugly = '010'
    start, end, n = 0, 3, len(b)
    res = 0
    while end <= n:
        if b[start:end] == ugly:
            res += 1
            start, end = start + 3, end + 3
        else:
            start, end = start + 1, end + 1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
