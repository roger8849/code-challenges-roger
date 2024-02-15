'''
28. Implement strStr()
Easy

Share
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
 
Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''
class Solution:
    # implemented this function just to validate if works or not.
    def strStrBuiltIn(self, haystack: str, needle: str) -> int:
        if not needle :
            return 0
        try:
            return haystack.index(needle)
        except:
            return -1

    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        # For the purpose of this problem, we will return 0 when needle is an empty string.
        if not needle :
            return 0
        # Right is the index of the size of the needle
        left, right = 0, len(needle)
        # Right cannot be greater than len of haystack to avoid index out of bounds exception
        while right <= len(haystack):
            # if slice is needle we found it.
            if haystack[left:right] == needle:
                return left
            # else then increase the index to keep looking.
            left, right = left + 1, right + 1
        return index
    
    def strStrOneIndex(self, haystack: str, needle: str) -> int:
        small_size = len(needle)
        n = len(haystack)

        for i in range(n):
            if i + small_size <= n:
                small_hay = haystack[i:i+small_size]
                # print(small_hay)
                if small_hay == needle:
                    return i
            else:
                return -1
        return -1

def main():
    solution = Solution()
    print('--- Built In python function  ---')
    print(solution.strStrBuiltIn('hello', 'll'))
    print(solution.strStrBuiltIn('aaaaa', 'bba'))
    
    print('--- Implementation ---')
    print(solution.strStr('hello', 'll'))
    print(solution.strStr('aaaaa', 'bba'))

if __name__ == "__main__":
    main()