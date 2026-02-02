# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next 
        slow.next = None
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # cur = head
        cur1 = head
        cur2 = prev
        while cur2:
            nxt1 = cur1.next
            nxt2 = cur2.next

            cur1.next = cur2
            cur2.next = nxt1

            cur1 = nxt1
            cur2 = nxt2
        
        # cur.next = None