'''
5. Longest Palindromic Substring
Solved
Medium
Topics
Companies
Hint

Given a string s, return the longest
palindromic
substring
in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.


'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0

        for i in range(len(s)):
            #odd lenght
            l, r = i, i

            while l >=0 and r < len(s) and s[l] == s[r]:
                if(r-l+1) > max_len:
                    res = s[l:r+1]
                    max_len = r - l + 1
                l -= 1
                r += 1
            
            # even lenght
            l, r = i, i + 1

            while l >=0 and r < len(s) and s[l] == s[r]:
                if(r-l+1) > max_len:
                    res = s[l:r+1]
                    max_len = r - l + 1
                l -= 1
                r += 1
        return res
