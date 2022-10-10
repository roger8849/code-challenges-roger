'''
https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    count = 0
    # Write your code here
    temp = n
    while temp != 0:
        digit =  temp % 10
        count = count + 1 if digit !=0 and n % digit == 0 else count
        temp = temp // 10
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)
        assert result == 3 if n == 123456789 else True 
        assert result == 3 if n == 114108089 else True 
        assert result == 6 if n == 110110015 else True 
        assert result == 2 if n == 121 else True 
        assert result == 2 if n == 33 else True 
        assert result == 2 if n == 44 else True 
        assert result == 2 if n == 55 else True 
        assert result == 2 if n == 66 else True 
        assert result == 2 if n == 77 else True 
        assert result == 2 if n == 88 else True 
        assert result == 5 if n == 106108048 else True 
        
    #     fptr.write(str(result) + '\n')

    # fptr.close()
