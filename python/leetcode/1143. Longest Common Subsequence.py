'''
1143. Longest Common Subsequence
Medium

Share
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
'''

class Solution:
    def helper(self, text1: str, text2: str, i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return  1 + self.helper(text1,text2,i+1,j+1)
        return max(self.helper(text1, text2, i+1, j), self.helper(text1, text2, i, j+1))
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # i, j = 0 ,0
        # return self.helper(text1, text2, i, j)
        m : int = len(text1)
        n : int = len(text2)
        if m < n:
            m, n, text1, text2 = n, m, text2, text1
        # arr=[[-1]*n]*m

        dp = [[0]*(n+1)]*(m+1)

        for i in range(m+1):
            for j in range(n+1):
                if i ==0 or j == 0:
                    dp[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

def main():
    solution = Solution()
    # text1 , text2 = "abcde", "ace" 
    # assert solution.longestCommonSubsequence(text1, text2) == 3

    # text1 , text2 = "abc", "abc" 
    # assert solution.longestCommonSubsequence(text1, text2) == 3

    # text1 , text2 = "abc", "def" 
    # assert solution.longestCommonSubsequence(text1, text2) == 0

    text1 , text2 = "abcba", "abcbcba" 
    assert solution.longestCommonSubsequence(text1, text2) == 0

if __name__ == "__main__":
    main()