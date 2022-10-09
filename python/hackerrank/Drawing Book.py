"""
Drawing Book
https://www.hackerrank.com/challenges/drawing-book/problem?h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&isFullScreen=false
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    # Flag that tells if should I start from page1 or not.
    shouldStartFromOne = True if p <= n//2 else False
    pageTurns = 0
    if shouldStartFromOne:
        pageTurns = p//2
    else:
        # Corner case at the end of the book.
        pageTurns = ((n-p)//2) + 1 if n-p == 1 and n%2 == 0 else (n-p)//2
    return pageTurns

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
