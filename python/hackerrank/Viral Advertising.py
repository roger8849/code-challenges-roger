

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    cumulative = 2
    shared = 5
    for i in range(2, n+1):
        shared = shared// 2 * 3
        cumulative += (shared // 2)
    return cumulative

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    # fptr.write(str(result) + '\n')

    # fptr.close()
