'''
1047. Remove All Adjacent Duplicates In String
Easy

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''
from queue import LifoQueue

class Solution:
    def removeDuplicates(self, s: str) -> str:
        string_stack = list()
        for letter in s:
            stack_length = len(string_stack)
            if stack_length == 0:
                string_stack.append(letter)
            else:
                top = string_stack[stack_length-1]
                if letter.lower() == top:
                    string_stack.pop()
                else:
                    string_stack.append(letter)

        return str().join(string_stack)

def main():
    solution = Solution()
    print(solution.removeDuplicates('abbaca'))
    print(solution.removeDuplicates('azxxzy'))

if __name__ == "__main__":
    main()