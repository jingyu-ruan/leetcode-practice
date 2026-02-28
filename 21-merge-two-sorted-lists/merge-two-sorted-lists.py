# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        dummy = ListNode()
        p = dummy
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                p.next = cur1
                cur1 = cur1.next
            else:
                p.next = cur2
                cur2 = cur2.next
            p = p.next
        while cur1:
            p.next = cur1
            cur1 = cur1.next
            p = p.next
        while cur2:
            p.next = cur2
            cur2 = cur2.next
            p = p.next
        p.next = None
        return dummy.next