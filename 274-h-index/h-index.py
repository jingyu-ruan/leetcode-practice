class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)
        res = 0
        for i in range(n):
            if citations[i] >= i + 1:
                res += 1
            else:
                return res
        return res