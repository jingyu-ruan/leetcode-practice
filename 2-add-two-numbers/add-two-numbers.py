# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10
            node = ListNode(total % 10)
            cur.next = node
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            total = l1.val + carry
            carry = total // 10
            node = ListNode(total % 10)
            cur.next = node
            cur = cur.next
            l1 = l1.next
        while l2:
            total = l2.val + carry
            carry = total // 10
            node = ListNode(total % 10)
            cur.next = node
            cur = cur.next
            l2 = l2.next

        if carry != 0:
            node = ListNode(carry)
            cur.next = node
            cur = cur.next

        cur.next = None
        return dummy.next
