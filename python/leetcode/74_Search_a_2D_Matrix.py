'''
74. Search a 2D Matrix
Medium

Share
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

from typing import List


class Solution:

    def binarySearch(self, row: List[int], target: int) -> bool:
        start, end = 0, len(row) - 1
        while start <= end:
            mid = start + (end - start)//2 # (start+end)//2 to avoid int overflow
            if row[mid] == target:
                return True
            elif row[mid] > target:
                end = mid - 1
            elif row[mid] < target:
                start = mid + 1
        else:
            return False

    def searchMatrixBS(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Using binary search in each row.
        '''
        for i in range(len(matrix)):
            row = matrix[i]
            found = self.binarySearch(row, target)
            if found: return found
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Using stair case algorithm. Starts at the top right element:

        if target > matrix [row][column] move down row++
        if target < matrix [row][column] move left col--
        if target == matrix [row][column] return True
        do this until
        column > 0 and row <= n -1 
        '''
        n, m = len(matrix), len(matrix[0])

        row, column = 0, m-1

        while column >= 0 and row <= n-1 :
            element = matrix[row][column]
            if element == target:
                return True
            elif target < element:
                column -= 1
            elif target > element:
                row += 1
        else:
            return False

def main():
    solution = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    assert solution.searchMatrixBS(matrix, target) == True
    assert solution.searchMatrix(matrix, target) == True

    
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    assert solution.searchMatrixBS(matrix, target) == False
    assert solution.searchMatrix(matrix, target) == False

if __name__ == "__main__":
    main()