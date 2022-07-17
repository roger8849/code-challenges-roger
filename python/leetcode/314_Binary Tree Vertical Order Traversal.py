'''
314. Binary Tree Vertical Order Traversal
Medium

Share
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class VisitedNode:
    def __init__(self, node, horizontalDistance):
        self.node = node
        self.horizontalDistance = horizontalDistance

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result, helperQueue = [], []
        visitedNodes = defaultdict(list)

        if not root:
            return result

        helperQueue.append(VisitedNode(root, 0))

        while helperQueue:
            visitedNode = helperQueue.pop(0)

            treeNode, horizontalDistance = visitedNode.node, visitedNode.horizontalDistance

            if treeNode:
                visitedNodes[horizontalDistance].append(treeNode.val)

                if treeNode.left:
                    helperQueue.append(VisitedNode(treeNode.left, horizontalDistance - 1))
                if treeNode.right:
                    helperQueue.append(VisitedNode(treeNode.right, horizontalDistance + 1))
        # map is ready
        return [visitedNodes[horizontalDistance] for horizontalDistance in sorted(visitedNodes.keys())]

    # Leetcode implementation
    def verticalOrderLeetcode(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                        
        return [columnTable[x] for x in sorted(columnTable.keys())]

def main():
    # root = [1,null,2,3]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(8)
    
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(0)

    root.right.left = TreeNode(1)
    root.right.right = TreeNode(7)
    
    
    root.left.right.left = TreeNode(5)
    
    root.right.left.right = TreeNode(2)

    sol = Solution()
    result = sol.verticalOrder(root)
    assert result == [[4],[9,5],[3,0,1],[8,2],[7]]

if __name__ == "__main__":
    main()