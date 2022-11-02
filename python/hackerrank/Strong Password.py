'''
Strong Password
https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    isUpperMissing = 0 if len(re.findall(r'[A-Z]',password)) > 0 else 1
    isLowerMissing = 0 if len(re.findall(r'[a-z]',password)) > 0 else 1
    isDigitsMissing = 0 if len(re.findall(r'[0-9]',password)) > 0 else 1
    isSpecialsMissing = 0 if len(re.findall(r'[!@#$%^&*()\-+]',password)) > 0 else 1

    length = 6 - n
    requiredMissing = isUpperMissing + isLowerMissing + isDigitsMissing + isSpecialsMissing
    return max(length, requiredMissing)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)
    '''
    7
    AUzs-nV
    '''
    assert answer == 1 if n == 7 and password == 'AUzs-nV' else True

    # fptr.write(str(answer) + '\n')

    # fptr.close()
