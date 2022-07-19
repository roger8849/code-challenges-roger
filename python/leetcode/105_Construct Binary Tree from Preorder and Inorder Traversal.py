'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

Add to List

Share
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTreeHelper(self, inorder: List[int], preorder: List[int], inorderStart: int, inorderEnd: int, preorderStart: int, preoderEnd: int) -> TreeNode:
        if inorderStart > inorderEnd:
            return None
        rootData = preorder[preorderStart]
        rootIndex = -1
        for i in range(inorderStart, inorderEnd + 1):
            if inorder[i] == rootData:
                rootIndex = i
                break
        
        leftInorderStart = inorderStart
        leftInorderEnd = rootIndex - 1
        leftPreorderStart = preorderStart + 1
        leftPreorderEnd = leftPreorderStart + leftInorderEnd - leftInorderStart

        rightInorderStart = rootIndex + 1
        rightInorderEnd = inorderEnd
        rightPreoderStart = leftPreorderEnd + 1
        rightPreoderEnd = preoderEnd

        root = TreeNode(rootData)
        root.left = self.buildTreeHelper(inorder, preorder, leftInorderStart, leftInorderEnd, leftPreorderStart, leftPreorderEnd)
        root.right = self.buildTreeHelper(inorder, preorder, rightInorderStart, rightInorderEnd, rightPreoderStart, rightPreoderEnd)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        return self.buildTreeHelper(inorder, preorder, 0, n-1, 0, n-1)