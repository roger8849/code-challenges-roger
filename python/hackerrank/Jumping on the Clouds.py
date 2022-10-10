'''
Jumping on the Clouds
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    goodCloud, i, count = 0 , 0, 0

    while i < n :
        count += 1
        if i + 2 < n and c[i+2] == goodCloud:
            i += 2
        else:
            i += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
