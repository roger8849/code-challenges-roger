'''
145. Binary Tree Postorder Traversal
Easy

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
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
    def postorderTraversalHelper(self, root: Optional[TreeNode], traversalList: List) -> _void:
        if root == None:
            return 
        self.postorderTraversalHelper(root.left, traversalList)
        self.postorderTraversalHelper(root.right, traversalList)
        traversalList.append(root.val)

        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = list() 
        self.postorderTraversalHelper(root, traversal)
        return traversal
def main():
    # root = [1,null,2,3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    sol = Solution()
    traversal = sol.postorderTraversal(root)
    assert traversal == [3,2,1]

    root = None
    traversal = sol.postorderTraversal(root)
    assert traversal == []

    root = TreeNode(1)
    traversal = sol.postorderTraversal(root)
    assert traversal == [1]
    


if __name__ == "__main__":
    main()