'''
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    common_prefix = ''
    #Base case if the list is empty
    if len(strs) == 0: return common_prefix
    #2nd. base case if the list has 1 element, then the element is the longest common prefix
    if len(strs) == 0: return strs[0]

    base_string = strs[0]
    print(range(len(base_string)))
    for i in range(len(base_string)):
        letter = base_string[i]
        print(letter)
        for j in range(1, len(strs)):
            # 1st part of the condition make sure that we don't have a index out of bounds.
            # 2nd part of the condition to see if we found the longest commond prefix
            if i >=len(strs[j]) or letter != strs[j][i] :
                return common_prefix
        common_prefix += letter
    
    # Assuming first element is the shortest string
    return common_prefix


def main():
    print(longestCommonPrefix(["flower","flow","flight"]))

if __name__ == "__main__":
    main()