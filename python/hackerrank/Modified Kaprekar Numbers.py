"""
Modified Kaprekar Numbers
https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def splitNum(n: int, digits: int):
    nStr = str(n)
    left, right = 0, 0
    leftSize = len(nStr)-digits
    left = int(nStr[:leftSize]) if leftSize > 0 else 0
    right = int(nStr[leftSize:])
    return left, right


def kaprekarNumbers(p, q):
    # Write your code here
    isInvalid = True
    for num in range(p, q+1):
        left, right = splitNum(pow(num,2),len(str(num)))
        if num == (left + right):
            isInvalid = False
            print(num, end=' ')

    if isInvalid:
        print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
