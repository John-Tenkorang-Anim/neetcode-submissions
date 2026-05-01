from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q = deque()
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            n = ListNode(total % 10)
            q.append(n)
            carry = total//10
            l1 , l2 = l1.next, l2.next

        while l1:
            total = l1.val + carry
            n = ListNode(total % 10)
            q.append(n)
            carry = total//10
            l1 = l1.next

        while l2:
            total = l2.val + carry
            n = ListNode(total % 10)
            q.append(n)
            carry = total//10
            l2 = l2.next

        if carry != 0:
            q.append(ListNode(carry))

        curr = head = q.popleft()
        while q:
            n = q.popleft()
            curr.next = n
            curr = curr.next

        return head
