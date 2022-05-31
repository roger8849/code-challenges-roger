'''
21. Merge Two Sorted Lists
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Fake head to not loose the first reference.
        result = fake_head = ListNode()
        # While both list has elements
        while list1 and list2 :
            if list1.val < list2.val:
                result.next = list1
                result = list1
                list1 = list1.next
            else:
                result.next = list2
                result = list2
                list2 = list2.next
        # If any of both list still has elements then assign them.
        if list1 or list2:
            result.next = list1 if list1 else list2
        return fake_head.next

def main():
    solution = Solution()
    a, a.next, a.next.next = ListNode(1), ListNode(2), ListNode(4)
    b, b.next, b.next.next = ListNode(1), ListNode(3), ListNode(4)
    print(solution.mergeTwoLists(a, b))

if __name__ == "__main__":
    main()