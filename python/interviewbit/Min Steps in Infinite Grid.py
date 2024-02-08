'''
Min Steps in Infinite Grid
Bookmark
Easy

Asked In:
Directi
Amazon
Problem Description

You are in an infinite 2D grid where you can move in any of the 8 directions

 (x,y) to 
    (x-1, y-1), 
    (x-1, y)  , 
    (x-1, y+1), 
    (x  , y-1),
    (x  , y+1), 
    (x+1, y-1), 
    (x+1, y)  , 
    (x+1, y+1) 
You are given a sequence of points and the order in which you need to cover the points.. Give the minimum number of steps in which you can achieve it. You start from the first point.

NOTE: This question is intentionally left slightly vague. Clarify the question by trying out a few cases in the “See Expected Output” section.



Input Format
Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.



Output Format
Return an Integer, i.e minimum number of steps.



Example Input
Input 1:

 A = [0, 1, 1]
 B = [0, 1, 2]


Example Output
Output 1:

 2


Example Explanation
Explanation 1:

 Given three points are: (0, 0), (1, 1) and (1, 2).
 It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
'''

class Solution:
    def coverPoints(self, X, Y):
        """Implements the solution of the minimum steps to go from (x1, y1) to (xn, yn)
        
        where (xi,yi) = (A[i], B[i]).
        
        Solution:
        
        It's a mathematical formula that stands that we need to try to always move in diagonal
        then after moving in diagonal we move in four directions: up, down, right, left. Basically the algorithm
        stands that the minimum steps to go from x(i), y(i) to x(i+1), y(i+1)
        is the maximum(abs(x_i - x_i+1), abs(y_i - y_+1))

        Args:
            X (_type_): points in the X Axis
            Y (_type_): points in the Y Axis

        Returns:
            _type_: minimum number of steps to go from x1,y1 to xn, yn
        """        
        ans = 0
        for i in range(len(X) - 1):
            ans += max(abs(X[i+1]-X[i]), abs(Y[i+1]-Y[i]))
        return ans
def main():
    X = [0, 1, 1]
    Y = [0, 1, 2]
    solution = Solution()

    assert solution.coverPoints(X,Y) == 2

    X = [-2]
    Y = [-7]
    assert solution.coverPoints(X,Y) == 0



if __name__ == "__main__":
    main()