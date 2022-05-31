'''
9. Palindrome Number
Easy
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
'''

class Solution:
    # Convert x variable to String and then use 2 pointers to check palindrome.
    # O(n) we have to iterate entire number
    # S(n) we use extra space to convert x to new string, memory is being used.
    def isPalindromeStr(self, x: int) -> bool:
        x = str(x)
        start, end = 0, len(x)-1

        while start < end:
            if not x[start] == x[end]:
                return False
            start += 1
            end -= 1

        return True

    # Implements the algorithm without converting to String
    # O(n/2) revert half of the number
    # S(1) do not use extra space to get the algorithm.
    def isPalindrome(self, x: int) -> bool:
        # Algorithm

        # First of all we should take care of some edge cases. All negative numbers are not palindrome, for example: -123 is not a palindrome since the '-' does not equal to '3'. So we can return false for all negative numbers.

        # Now let's think about how to revert the last half of the number. For number 1221, if we do 1221 % 10, we get the last digit 1, to get the second to the last digit, we need to remove the last digit from 1221, we could do so by dividing it by 10, 1221 / 10 = 122. Then we can get the last digit again by doing a modulus by 10, 122 % 10 = 2, and if we multiply the last digit by 10 and add the second last digit, 1 * 10 + 2 = 12, it gives us the reverted number we want. Continuing this process would give us the reverted number with more digits.

        # Now the question is, how do we know that we've reached the half of the number?

        # Since we divided the number by 10, and multiplied the reversed number by 10, when the original number is less than the reversed number, it means we've processed half of the number digits.

        # Negative numbers are never a palindrome. 
        # Also if last digit is 0 first digit must be 0 only 0 satisfies that condition
        if x < 0 or (x % 10 == 0 and not x == 0):
            return False

        revertedNumber = int()
        while x > revertedNumber :
            revertedNumber = (revertedNumber * 10) + (x % 10)
            x //= 10

        # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == revertedNumber or x == revertedNumber//10

def main():
    solution = Solution()
    print('--- Using String ---')
    print(solution.isPalindromeStr(121))
    print(solution.isPalindromeStr(-121))
    print(solution.isPalindromeStr(10))
    print(solution.isPalindromeStr(1000001))
    
    print('--- Using numbers only ---')
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))
    print(solution.isPalindrome(1000001))

if __name__ == "__main__":
    main()