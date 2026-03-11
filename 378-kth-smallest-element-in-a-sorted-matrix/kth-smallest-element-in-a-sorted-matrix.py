import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        1  5  9
        10 11 13
        12 13 15
        '''
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(heap)
        for _ in range(k):
            val, i, j = heapq.heappop(heap)
            if j < n - 1:
                heapq.heappush(heap, (matrix[i][j+1], i, j + 1))
        
        return val