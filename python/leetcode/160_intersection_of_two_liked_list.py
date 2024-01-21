'''
160. Intersection of Two Linked Lists
Easy

9834

951

Add to List

Share
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
 

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
Accepted
1,015,348
Submissions
1,969,609
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getListSize(self, head: ListNode) -> int:
        size = 0
        if not head: return size
        while head:
            size += 1
            head = head.next
        return size



    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_size = self.getListSize(headA) # find the size of the first linked list.
        b_size = self.getListSize(headB) # find the size of the second linked list.

        difference = int()
        
        # This portion of code put both elements in the same start
        if a_size > b_size: # If linked list A is bigger then jump the positions
            difference = a_size - b_size
            for i in range(difference):
                headA = headA.next
        elif b_size > a_size:
            difference = b_size - a_size # If linked list B is bigger then jump the positions
            for i in range(difference):
                headB = headB.next
        # The two linked list are at the same position then iterate both at the same time to find the intersection.
        while headA is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        # No intersection found then return None
        return None

def main():
    solution = Solution()
    a, a.next, a.next.next, a.next.next.next, a.next.next.next.next = ListNode(4), ListNode(1), ListNode(8), ListNode(4), ListNode(5)
    b, b.next, b.next.next, b.next.next.next, b.next.next.next.next, b.next.next.next.next.next = ListNode(5), ListNode(6), ListNode(1), ListNode(8), ListNode(4), ListNode(5)
    
    a_size = solution.getListSize(a)
    b_size = solution.getListSize(b)
    
    assert a_size == 5
    assert b_size == 6

    result = solution.getIntersectionNode(a,b)
    print(result.next)


if __name__ == "__main__":
    main()