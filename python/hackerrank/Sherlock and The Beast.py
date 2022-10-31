'''
Sherlock and The Beast
https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Write your code here
    three, five = '33333', '555'
    q3, r3 = divmod(n, 3)
    if r3 == 0: 
        return (five * q3)
    # decrements quotient of q3 and increments r3 to see if divisible by 5
    # this is done so that we get as many 5's as possible 
    while q3 > 0: 
        r3 += 3
        q3 -= 1         
        q, r = divmod(r3, 5)
        if r == 0: 
            return ((five * q3) + (three * q))
            
        
    return -1

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decent = decentNumber(n)
        print(decent)

    '''
    STDIN   Function
    -----   --------
    4       t = 4
    1       n = 1 (first test case)
    3       n = 3 (second test case)
    5
    11
    '''
