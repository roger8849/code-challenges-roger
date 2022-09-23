'''
118. Pascal's Triangle
Easy

Share
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
Accepted
1,001,925
Submissions
1,461,620
'''


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = list()
        
        for i in range(numRows):
            currentLevel = [1]*(i+1)
            # base cases
            if i > 1:
                prevLevel = result[i-1]
                for j in range(1,len(currentLevel) - 1):
                    currentLevel[j] = prevLevel[j-1] + prevLevel[j]
            result.append(currentLevel)
        return result


def main():
    solution = Solution()

    assert solution.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

if __name__ == "__main__":
    main()
