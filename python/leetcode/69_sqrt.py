'''
69. Sqrt(x)
Easy

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

Constraints:

0 <= x <= 231 - 1
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        start, end, ans = 1, x, 0
        while start <= end:
            mid = start + (end - start)//2 # (start+end)//2 to avoid int overflow
            # Exact root square
            if mid == x // mid:
                return mid
            elif mid < x//mid:
                # candidate but keep looking for a bigger candidate
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans

def main():
    solution = Solution()
    x = 4
    print(f'Integer sqrt of {x} is {solution.mySqrt(x)}')
    x = 8
    print(f'Integer sqrt of {x} is {solution.mySqrt(x)}')

if __name__ == "__main__":
    main()