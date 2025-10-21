# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None

        prev = None
        curr = l2

        while curr:
            nxt_temp = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_temp

        l2 = prev
        l1 = head
        while l2:
            l2_nxt = l2.next
            l1_nxt = l1.next

            l1.next = l2
            l2.next = l1_nxt
            
            l1 = l1_nxt
            l2 = l2_nxt
        

        