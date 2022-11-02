'''
Sum vs XOR
https://www.hackerrank.com/challenges/sum-vs-xor/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Write your code here
    """
        only count number of zero and return in the power of 2.
    """
    binN = "{0:b}".format(n)
    return pow(2, binN.count('0')) if n > 0 else 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
