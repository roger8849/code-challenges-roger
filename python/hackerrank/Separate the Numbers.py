'''
Separate the Numbers
https://www.hackerrank.com/challenges/separate-the-numbers/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    n = len(s)
    # Iterate till the half of the str next number will be next half.
    for i in range(1, n //2 + 1):
        # generate number
        firstInt = int(s[:i])
        count = 0
        genString = ''
        while len(genString) < n:
            # generate rest of the string based on first number
            genString += str(firstInt + count)
            count = count + 1
        # if Strings are equals we found the number return to stop
        if genString == s:
            print(f'YES {firstInt}') 
            return
    # if no number was found then print NO
    print('NO')
        
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

