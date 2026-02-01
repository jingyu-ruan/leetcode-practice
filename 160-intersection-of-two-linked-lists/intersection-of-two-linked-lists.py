# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1 = headA
        cur2 = headB
        while cur1 != cur2:

            if not cur1:
                cur1 = headB
            else:
                cur1 = cur1.next
            
            if not cur2:
                cur2 = headA
            else:
                cur2 = cur2.next
        
        return cur1