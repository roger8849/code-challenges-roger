'''
K Largest Elements
https://www.interviewbit.com/problems/k-largest-elements/
Bookmark
Easy
60.5% Success

Asked In:
Amazon
Delhivery
Flipkart
Problem Description

Given an 1D integer array A of size N you have to find and return the B largest elements of the array A.

NOTE:

Return the largest B elements in any order you like.


Problem Constraints
1 <= N <= 105

1 <= B <= N

1 <= A[i] <= 103



Input Format
First argument is an 1D integer array A

Second argument is an integer B.



Output Format
Return a 1D array of size B denoting the B largest elements.



Example Input
Input 1:

 A = [11, 3, 4]
 B = 2
Input 2:

 A = [11, 3, 4, 6]
 B = 3


Example Output
Output 1:

 [11, 4]
Output 2:

 [4, 6, 11]


Example Explanation
Explanation 1:

 The two largest elements of A are 11 and 4

Explanation 2:
 The three largest elements of A are 11, 4 and 6

'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        from heapq import heapify, heappush, heappop

        largest = []
        heapify(largest)

        for num in A:
            if len(largest) == B:
                # minNum = heappop(largest)
                # if num > minNum:
                #     heappush(largest, num)
                # else:
                #     heappush(largest, minNum)
                heappush(largest, max(num, heappop(largest)))
            else:
                heappush(largest, num)

        return largest
        