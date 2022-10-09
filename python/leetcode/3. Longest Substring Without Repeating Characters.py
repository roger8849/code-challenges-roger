'''
3. Longest Substring Without Repeating Characters
Medium

29148

1240

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
Accepted
3,889,252
Submissions
11,528,821
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        li, ri, n, maxLen = 0, 0, len(s), 0
        uniqueLetters = set()

        while li < n:
            if ri == n:
                break
            if s[ri] in uniqueLetters:
                uniqueLetters.remove(s[li])
                li += 1
            else:
                uniqueLetters.add(s[ri])
                maxLen = max(len(uniqueLetters), maxLen)
                ri += 1
        return maxLen


def main():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("au") == 2

if __name__ == "__main__":
    main()