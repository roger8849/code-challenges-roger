"""
https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
"""

#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    sockCount = defaultdict(int)

    for sock in ar:
        sockCount[sock] += 1
    return sum([count//2 for count in sockCount.values() if count > 0])
    

if __name__ == '__main__':
    

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)


