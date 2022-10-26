'''
Palindrome Index
https://www.hackerrank.com/challenges/palindrome-index/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def isPalindrome(s: str, start: int, end: int) -> bool:
    # start, end = 0, len(s) - 1
    while start < end:
        if not s[start].lower() == s[end].lower():
            return False
        start += 1; end -= 1
    return True

def palindromeIndex(s):
    # Write your code here
    # this if the string is empty or contain spaces is a Palindrome
    if not s or s.isspace():
        return -1
    start, end = 0, len(s) - 1
    
    while start < end :
        if s[start] == s[end]:
            start += 1; end -= 1
        else:
            # Cut the array in the start or the end
            if isPalindrome(s, start + 1, end):
                return start
            elif isPalindrome(s, start, end-1):
                return end
            else:
                return -1
    # String is already a palindrome
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
