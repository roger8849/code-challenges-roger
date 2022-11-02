'''
Lisa's Workbook
https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    res = 0
    pageCount = 0
    for problems in arr:
        # Start with a new page everytime you start a chapter
        pageCount += 1
        # iterate over the problems per chapter
        for i in range(1, problems + 1):
            # if problem matches the page then it's a perfect problem
            if i == pageCount:
                res += 1
            # increase the page if problem is multiple of k and not the limit of problems.
            # The limit of problems avoid to generate a blank page with no content.
            if i % k  == 0 and i != problems:
                pageCount += 1
    return res

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    assert result == 4 if n == 5  and k == 3 and arr == [4,2,6,1,10] else True
    assert result == 8 if n == 10  and k == 5 and arr == [3,8,15,11,14,1,9,2,24,31] else True

    # fptr.write(str(result) + '\n')

    # fptr.close()
