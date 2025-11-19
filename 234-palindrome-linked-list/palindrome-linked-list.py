# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow2 = slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        cur1 = prev
        while cur1 and slow2:
            if cur1.val != slow2.val:
                return False
            cur1 = cur1.next
            slow2 = slow2.next
        return True
        

