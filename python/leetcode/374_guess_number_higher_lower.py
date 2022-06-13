'''
374. Guess Number Higher or Lower
Easy

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    to_guess = 6
    if num == 6:
        return 0
    elif num > 6:
        return -1
    elif num < 6:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        '''
            1 <= n <= 231 - 1
            1 <= pick <= n
        '''
        start, end = 1, n
        while start <= end:
            mid = start + (end - start)//2 # (start+end)//2 to avoid int overflow
            guess_ans = guess(mid)
            if guess_ans == -1:
                end = mid - 1
            elif guess_ans == 1:
                start = mid + 1
            else:
                return mid
        
        
def main():
    solution = Solution()
    print(f'Number to guess is 6 and guess number returned: {solution.guessNumber(10)}')

if __name__ == "__main__":
    main()
