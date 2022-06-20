'''
70. Climbing Stairs
Easy

Share
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
Accepted
1,630,136
Submissions
3,180,433
'''

class Solution:
    def climbStairsHelper(self, n, memory):
        if n in memory:
            return memory[n]
        small_answer = self.climbStairsHelper(n-1) + self.climbStairsHelper(n-2)
        memory[n] = small_answer
        return memory[n]
        
    def climbStairs(self, n: int) -> int:
        memory = {0:0, 1:1, 2:2}
        return self.climbStairsHelper(n, memory)


def main():
    solution = Solution()


if __name__ == '__main__':
    main()