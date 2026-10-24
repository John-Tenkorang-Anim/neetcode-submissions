# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev

            # Find the kth node
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            group_head = group_prev.next

            # Disconnect the current group
            kth.next = None

            # Reverse exactly k nodes
            new_head = self.reverse(group_head)

            # Reconnect the reversed group
            group_prev.next = new_head
            group_head.next = group_next

            # Move to the next group
            group_prev = group_head


    def reverse(self, node):
        prev = None
        curr = node

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        