'''
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''

from typing import List

#Best approach do not use extra space. O(n) S(1)
def reverseString(s: List[str]) -> None:
    """
        Do not return anything, modify s in-place instead.
    """
    # Two indexes to not use extraspace to store the reverse
    start, end = 0, len(s) - 1

    while start < end:
        s[start], s[end] = s[end], s[start]
        start, end = start+1, end-1
    else:
        print(f'String reversed {s}')

# Iterate the string two times, innefficient and use extra space O(n) S(n)
def reverseStringUsingStack(s: List[str]) -> None:
    reversed_stack = []

    while len(s) > 0 :
        reversed_stack.append(s.pop())
    
    while len(reversed_stack) > 0 :
        s.append(reversed_stack.pop())
    print(f'String reversed {s}')

def main():
    s = list(input('Enter a string to reverse: '))
    reverseString(s)
    reverseStringUsingStack(s)

if __name__ == "__main__":
    main()
