# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        m = 0
        while curr:
            m += 1
            curr = curr.next

        pos = m - n
        if pos == 0:
            head = head.next
            return head

        first = head
        for i in range(m - 1):
            if (i + 1) == pos:
                first.next = first.next.next
                break
            first = first.next

        return head


            

        
        