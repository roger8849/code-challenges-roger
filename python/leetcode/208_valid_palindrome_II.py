'''
680. Valid Palindrome II
Easy

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
Accepted
501,150
Submissions
1,271,812
'''

def isPalindrome(s: str, start: int, end: int) -> bool:

    # start, end = 0, len(s) - 1

    while start < end:
        if not s[start].lower() == s[end].lower():
            return False
        
        start += 1; end -= 1
                
    return True


def validPalindrome(s: str) -> bool:
    # this if the string is empty or contain spaces is a Palindrome
    if not s or s.isspace():
        return True
    start, end = 0, len(s) - 1

    while start < end :
        if s[start] == s[end]:
            start += 1; end -= 1
        else:
            # Cut the array in the start or the end
            if isPalindrome(s, start + 1, end) or isPalindrome(s, start, end-1):
                return True
            else:
                return False
    return True


def main():
    print(validPalindrome('aba'))
    print(validPalindrome('abca'))
    print(validPalindrome('abc'))

if __name__ == "__main__":
    main()