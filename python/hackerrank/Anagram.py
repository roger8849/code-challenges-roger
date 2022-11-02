'''
Anagram
https://www.hackerrank.com/challenges/anagram/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    n = len(s)
    if not n % 2 == 0:
        return -1
    mid = n//2
    first, second = Counter(s[:mid]), Counter(s[mid:])
    return sum( (first - second).values())

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
