'''
64. Minimum Path Sum
Medium

Share
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
'''

from typing import List

class Solution:
    # non optimal solution     
    def minPathRecursive(self, i:int, j:int, n:int, m:int, grid:List[List[int]]) -> int:
        if i == m-1 and j == n-1:
            return grid[m-1][n-1]
        
        if i == m-1:
            return grid[i][j] + self.minPathRecursive(i, j+1, n, m, grid)
        if j == n-1:
            return grid[i][j] + self.minPathRecursive(i+1, j, n, m, grid)
        return grid[i][j] + min(
                self.minPathRecursive(i+1, j, n, m, grid),
                self.minPathRecursive(i, j+1, n, m, grid)
            )
    
    def minPathRecursiveMemory(self, i:int, j:int, n:int, m:int, grid:List[List[int]], memory:List[List[int]]) -> int:
        if memory[i][j] == -1:
            if i == m-1 and j == n-1:
                memory[i][j] = grid[m-1][n-1]
            elif i == m-1:
                memory[i][j] = grid[i][j] + self.minPathRecursiveMemory(i, j+1, n, m, grid, memory)
            elif j == n-1:
                memory[i][j]= grid[i][j] + self.minPathRecursiveMemory(i+1, j, n, m, grid, memory)
            else:
                memory[i][j] = grid[i][j] + min(
                        self.minPathRecursiveMemory(i+1, j, n, m, grid, memory),
                        self.minPathRecursiveMemory(i, j+1, n, m, grid, memory)
                    )
        return memory[i][j]
    def minPathDp(self, n:int, m:int, grid:List[List]):
        memory = [[ -1 for j in range(n) ] for i in range(m)]
        
        memory[m-1][n-1] = grid[m-1][n-1]
        
        # Initialize column n-1
        for i in range(m-2, -1,-1):
            memory[i][n-1] = grid[i][n-1] + memory[i+1][n-1]
        
        for j in range(n-2, -1,-1):
            memory[m-1][j] = grid[m-1][j] + memory[m-1][j+1]
            for i in range(m-2, -1,-1):
                memory[i][j] = grid[i][j] + min(memory[i+1][j], memory[i][j+1])
        return memory[0][0]
    
    def minPathDp2(self, n:int, m:int, grid:List[List]):
        mem = [ -1 for i in range(m)]
        mem_j_1 = [ -1 for j in range(m) ]
        mem_j_1[m-1] = grid[m-1][n-1]
        # Initialize column n-1
        for i in range(m-2, -1,-1):
            mem_j_1[i] = grid[i][n-1] + mem_j_1[i+1]
        
        for j in range(n-2, -1,-1):
            mem[m-1] = grid[m-1][j] + mem_j_1[m-1]
            for i in range(m-2, -1,-1):
                mem[i] = grid[i][j] + min(mem[i+1], mem_j_1[i])
            mem_j_1 = mem
        return mem_j_1[0]
        
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        
        # memory = [[ -1 for j in range(n) ] for i in range(m)]
        # print(memory)
        # return self.minPathRecursive(0, 0, n, m, grid)
        # return self.minPathRecursiveMemory(0, 0, n, m, grid, memory)
        # return self.minPathDp(n, m, grid)
        return self.minPathDp2(n, m, grid)
        