'''
Happy ladybugs
https://www.hackerrank.com/challenges/happy-ladybugs/forum
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    # First check if there are no unique chars rather than spaces.
    for i in set(b):
        if b.count(i) == 1 and i != '_':
            return "NO"

    
    # if there is no space to move. then check if ladybugs already happy.
    if b.count('_') == 0:
        left, right = 0,1
        while right < len(b) - 1:
            # If equals keep checking.
            if b[left] == b[right]:
                right += 1
            else:
                # This means ladybug is alone in her position.
                if right - left == 1:
                    return "NO"
                # Noit alone then check for the next char
                else:
                    left, right = right, right +1
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
