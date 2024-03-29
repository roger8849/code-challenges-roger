'''
String Construction
https://www.hackerrank.com/challenges/string-construction/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    # Write your code here
    seen = set(s)
    return len(seen)
    # cost = 0
    # for letter in s:
    #     if not letter in seen:
    #         seen.add(letter)
    #         cost += 1
    # return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
