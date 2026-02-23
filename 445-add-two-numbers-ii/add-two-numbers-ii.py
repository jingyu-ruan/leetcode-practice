# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = '', ''
        cur = l1
        while cur:
            num1 += str(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            num2 += str(cur.val)
            cur = cur.next
        num = str(int(num1) + int(num2))
        dummy = ListNode(0)
        cur = dummy
        for ch in num:
            node = ListNode(int(ch))
            cur.next = node
            cur = cur.next
        cur.next = None
        return dummy.next