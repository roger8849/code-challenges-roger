'''
https://www.hackerrank.com/challenges/sherlock-and-squares/problem?h_r=next-challenge&h_v=zen
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    higherA = int(math.ceil(math.sqrt(a)))
    lowerB = int(math.floor(math.sqrt(b)))
    if higherA > lowerB:
        return 0
    else:
        return lowerB - higherA + 1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        '''
            4
            3 9
            17 24
            35 70
            100 1000
        '''
        assert result == 2 if a == 3 and b == 9 else True
        assert result == 0 if a == 17 and b == 24 else True
        assert result == 3 if a == 35 and b == 70 else True
        assert result == 22 if a == 100 and b == 1000 else True

    #     fptr.write(str(result) + '\n')

    # fptr.close()
