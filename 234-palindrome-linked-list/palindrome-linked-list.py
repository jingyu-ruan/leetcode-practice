# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        D 1 2
        '''
        if not head.next:
            return True
        dummy = ListNode(0, head)
        fast = slow = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        p2 = slow.next
        slow.next = None
        p1 = head
        prev = None
        while p2:
            nxt = p2.next
            p2.next = prev
            prev = p2
            p2 = nxt
        p2 = prev
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
