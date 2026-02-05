# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        D 3 2 0 4
        s f
        '''
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                fast = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                
                return fast
        
        return None