'''
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Need a fake head to start iterating.
        fake_head = ListNode(0)
        result = fake_head
        carry = int()
        
        # l1 contains more elements, or l2 contains more elements or carry is 1 
        while l1 or l2 or carry :
            #print(f'First value {first.val} Second value{second.val}')
            
            # If l1 or l2 is not None then val otherwise 0 to avoid NPE
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry

            # Carry contains the value to add to next iteration, digit contains the current sum
            carry, digit = divmod(sum , 10)
            
            result.next = ListNode(digit) 
            result = result.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return fake_head.next

def main():
    solution = Solution()
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    print(solution.addTwoNumbers(a, b))
    
    a = ListNode(0)
    b = ListNode(0)
    print(solution.addTwoNumbers(a, b))

    a, a.next, a.next.next, a.next.next.next, 
    a.next.next.next.next, a.next.next.next.next.next,
    a.next.next.next.next.next.next  = ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9)
    
    b, b.next, b.next.next, b.next.next.next = ListNode(9), ListNode(9), ListNode(9), ListNode(9) 
    print(solution.addTwoNumbers(a, b))


if __name__ == "__main__":
    main()