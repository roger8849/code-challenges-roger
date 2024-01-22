'''
94. Binary Tree Inorder Traversal
Easy

Share
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
from inspect import _void
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversalHelper(self, root: Optional[TreeNode], traversalList: List) -> _void:
        if root == None:
            return 
        self.inorderTraversalHelper(root.left, traversalList) # Visit left subtree
        traversalList.append(root.val) # Visit the data
        self.inorderTraversalHelper(root.right, traversalList) # Visit right subtree

        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = list()
        self.inorderTraversalHelper(root, traversal)
        return traversal
def main():
    # root = [1,null,2,3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    sol = Solution()
    traversal = sol.inorderTraversal(root)
    assert traversal == [1,3,2]

    root = None
    traversal = sol.inorderTraversal(root)
    assert traversal == []

    root = TreeNode(1)
    traversal = sol.inorderTraversal(root)
    assert traversal == [1]
    


if __name__ == "__main__":
    main()