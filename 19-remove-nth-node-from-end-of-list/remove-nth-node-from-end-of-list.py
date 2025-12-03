# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy

        for i in range(n):
            fast = fast.next

        while fast.next and fast and slow:
            fast = fast.next
            slow = slow.next
        
        nxt = slow.next.next
        slow.next = nxt

        return dummy.next