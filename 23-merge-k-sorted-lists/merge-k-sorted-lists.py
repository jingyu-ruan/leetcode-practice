# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for lst in lists:
            cur = lst
            while cur:
                heapq.heappush(heap, cur.val)
                cur = cur.next
        
        dummy = ListNode(0)
        cur = dummy
        while heap:
            v = heapq.heappop(heap)
            cur.next = ListNode(v)
            cur = cur.next
        
        return dummy.next