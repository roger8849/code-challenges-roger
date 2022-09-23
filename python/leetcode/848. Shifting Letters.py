"""
848. Shifting Letters
Medium

1048

104

Add to List

Share
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

 

Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.
Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
shifts.length == s.length
0 <= shifts[i] <= 109
"""


from typing import List


class Solution:
    def shiftString(self, char: str, factor: int) -> str:
        aFactor, zFactor = ord('a'), ord('z')
        charFactor = ord(char) + factor
        if charFactor < zFactor:
            shiftFactor = charFactor  
        else:
            shiftFactor = charFactor 
            while shiftFactor > zFactor:
                shiftFactor = shiftFactor + aFactor - zFactor - 1
        ans = chr(shiftFactor) 
        return ans

    def shiftingLettersSlow(self, s: str, shifts: List[int]) -> str:
        shiftedList = list(s)
        for i in range(len(shifts)):
            for j in range(i+1):
                shiftedList[j] = self.shiftString(shiftedList[j], shifts[i])
        return "".join(shiftedList)
    
    def shiftingLetters(self, S, shifts):
        ans = []
        X = sum(shifts) % 26
        for i, c in enumerate(S):
            index = ord(c) - ord('a')
            ans.append(chr(ord('a') + (index + X) % 26))
            X = (X - shifts[i]) % 26

        return "".join(ans)

def main():
    solution = Solution()

    s, arr = "abc",[3,5,9]
    ans = solution.shiftingLetters(s, arr)
    assert ans == "rpl"
    
    s, arr = "aaa",[1,2,3]
    ans = solution.shiftingLetters(s, arr)
    assert ans == "gfd"
    
    s, arr = "bad",[10,20,30]
    ans = solution.shiftingLetters(s, arr)
    assert ans == "jyh"
    
    s, arr = "mkgfzkkuxownxvfvxasy",[505870226,437526072,266740649,224336793,532917782,311122363,567754492,595798950,81520022,684110326,137742843,275267355,856903962,148291585,919054234,467541837,622939912,116899933,983296461,536563513]
    ans = solution.shiftingLetters(s, arr)
    # assert ans == "jyh"



if __name__ == "__main__":
    main()