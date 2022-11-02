'''
Caesar Cipher
https://www.hackerrank.com/challenges/caesar-cipher-1/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    n = len(s)
    newAscii = k % 26
    newS = ''
    for letter in s:
        if letter.isalpha():
            aIncrement = ord('A') if letter.isupper() else ord('a')
            val = ord(letter) - aIncrement + newAscii
            newS = (
                newS + chr(val-26 + aIncrement) if val >= 26 
                else newS + chr(val + aIncrement)
            )
        else:
            newS += letter
    return newS
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

