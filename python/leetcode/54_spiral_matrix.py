'''
54. Spiral Matrix
Medium

Share
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

from tracemalloc import start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list()
        
        m = len(matrix)
        n = len(matrix[0])
        
        start_row, end_row = 0, m - 1
        start_column, end_column = 0, n - 1

        count = 0
        total_elements = n*m

        while start_row <= end_row and start_column <= end_column:
            # traversing up row.
            index = start_column
            while index <= end_column:
                result.append(matrix[start_row][index])
                index += 1
                count += 1
            if count == total_elements: return result

            # traversing right column
            start_row += 1
            index = start_row
            while index <= end_row:
                result.append(matrix[index][end_column])
                index += 1
                count += 1
            if count == total_elements: return result
            
            # traversing bottom row
            end_column -= 1
            index = end_column
            while index >= start_column:
                result.append(matrix[end_row][index])
                index -= 1
                count += 1
            if count == total_elements: return result
            
            # Traversing left column
            end_row -= 1
            index = end_row
            while index >= start_row:
                result.append(matrix[index][start_column])
                index -=1
                count += 1
            if count == total_elements: return result
            
            # Last increment for next iteration.
            start_column += 1

        return result


def main():
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = solution.spiralOrder(matrix)
    assert result == [1,2,3,6,9,8,7,4,5]



    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    result = solution.spiralOrder(matrix)
    assert result == [1,2,3,4,8,12,11,10,9,5,6,7]


if __name__ == "__main__":
    main()