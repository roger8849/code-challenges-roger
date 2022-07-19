'''
Inorder Traversal of Cartesian Tree
Medium
131
23
Asked In:
Amazon
Facebook
Given an inorder traversal of a cartesian tree, construct the tree.

Cartesian tree :  is a heap ordered binary tree, where the root is greater than all the elements in the subtree.

Note: You may assume that duplicates do not exist in the tree.

Example :

Input : [1 2 3]

Return :   
          3
         /
        2
       /
      1
Note:You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a question? Checkout Sample Codes for more details.
submission-count
28821
successful submissions.
'''

# Definition for a  binary tree node
import math


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
    def buildTreeHelper(self, inorder, start, end):
        if start > end:
            return None
        maxValue = -math.inf
        maxIndex = -1
        for i in range(start, end + 1):
            if inorder[i] > maxValue:
                maxValue = inorder[i]
                maxIndex = i
        root = TreeNode(maxValue)
        root.left = self.buildTreeHelper(inorder, start, maxIndex-1)
        root.right = self.buildTreeHelper(inorder, maxIndex + 1, end)
        return root
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, inorder):
        if not inorder:
            return None
        return self.buildTreeHelper(inorder, 0, len(inorder) - 1)