# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None # break the link to make it independent 2 parts
        second = self.reverse(second)
        first = head

        cur = dummy = ListNode(0)
        while first and second:
            next_first = first.next
            next_second = second.next

            cur.next = first
            cur = cur.next

            cur.next = second
            cur = cur.next

            first = next_first
            second = next_second


        cur.next = first if first else second
        head = dummy.next
        
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head = prev
        return head
        