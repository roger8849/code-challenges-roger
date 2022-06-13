'''
367. Valid Perfect Square
Easy

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
Accepted
378,700
Submissions
878,430
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end, = 1, num
        while start <= end:
            mid = start + (end - start)//2 # (start+end)//2 to avoid int overflow
            # Exact root square
            if mid * mid == num:
                return True
            elif mid < num//mid:
                start = mid + 1
            else:
                end = mid - 1
        return False

def main():
    solution = Solution()
    x = 4
    print(f'Is {x} a perfect square? {solution.isPerfectSquare(x)}')
    x = 8
    print(f'Is {x} a perfect square? {solution.isPerfectSquare(x)}')
    x = 5
    print(f'Is {x} a perfect square? {solution.isPerfectSquare(x)}')

if __name__ == "__main__":
    main()