"""
Super reduced string
https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    string_stack = list()
    for letter in s:
        if not string_stack:
            string_stack.append(letter)
        else:
            top = string_stack[-1]
            if letter.lower() == top:
                string_stack.pop()
            else:
                string_stack.append(letter)
    return str().join(string_stack) if string_stack else "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
