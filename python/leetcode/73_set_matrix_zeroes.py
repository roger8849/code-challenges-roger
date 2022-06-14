'''
73. Set Matrix Zeroes
Medium

Share
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()

        # Identify rows and colmuns
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        # replace values
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    if i in rows or j in columns:
                        matrix[i][j] = 0



def main():
    solution = Solution()

    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    solution.setZeroes(matrix)
    assert matrix == [[1,0,1],[0,0,0],[1,0,1]]


    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution.setZeroes(matrix)
    assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


if __name__ == "__main__":
    main()