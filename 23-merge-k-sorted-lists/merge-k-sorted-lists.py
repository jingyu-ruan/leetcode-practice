# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        i = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, i, node))
                i += 1
        dummy = ListNode(0)
        cur = dummy
        while heap:
            v, j, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                i += 1
            cur.next = node
            cur = cur.next
        cur.next = None
        return dummy.next