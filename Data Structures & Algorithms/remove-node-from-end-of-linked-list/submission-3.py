# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None:
            return None

        # count the total number of nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        

        prev = dummy = ListNode(0)
        dummy.next = head

        pnt = head
        for _ in range(count - n):
            prev = pnt
            pnt = pnt.next
        

        prev.next = pnt.next
        
        return dummy.next


        
        