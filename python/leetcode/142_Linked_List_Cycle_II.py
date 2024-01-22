'''
142. Linked List Cycle II
Medium

Share
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 
Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # S(n) using set as extra space
    def hasCycleUsingExtraMem(self, head: Optional[ListNode]) -> bool:
        elements = set()
        
        while head:
            if head in elements:
                return head
            elements.add(head)
            head = head.next
        else:
            return None



    # S(1) solution no extra space
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If there is a cycle in the linkedlist eventually they will meet each other.
            if slow == fast:
                # Cycle detectect, now move slow and fast at the same pace
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                else:
                    # They met at the intersection due a mathematical formula
                    # fast pointer - slow pointer is the size of the loop.
                    return slow
        else:
            return None

def main():
    pass

if __name__ == "__main__":
    main()
