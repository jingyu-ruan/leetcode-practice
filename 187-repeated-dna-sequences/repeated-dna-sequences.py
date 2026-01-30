class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []
        l = 0
        res = set()
        occur = set()
        for r in range(9, n):
            gene = s[l:r+1]
            if gene in occur:
                res.add(gene)
            occur.add(gene)
            l += 1
        return list(res)