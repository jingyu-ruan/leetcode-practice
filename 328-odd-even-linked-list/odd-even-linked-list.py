# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1 2 3 4 5
        o e o e
        '''
        if not head or not head.next:
            return head
        
        odd_cur = head
        even_cur = head.next
        second = head.next
        while odd_cur.next and even_cur.next:
            odd_next = odd_cur.next.next
            even_next = even_cur.next.next
            odd_cur.next = odd_next
            even_cur.next = even_next
            odd_cur = odd_cur.next
            even_cur = even_cur.next
        if even_cur:
            even_cur.next = None
        odd_cur.next = second
        return head
        

