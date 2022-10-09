"""
https://www.hackerrank.com/challenges/picking-numbers/problem?h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    count = Counter(a)
    maxSubSize = 0
    # constraint limit.
    for i in range(1,100):
        maxSubSize = max(maxSubSize, count[i]+count[i+1])
    return maxSubSize


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    # fptr.write(str(result) + '\n')

    # fptr.close()
