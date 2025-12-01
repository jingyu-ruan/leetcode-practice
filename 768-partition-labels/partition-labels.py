from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = Counter(s)
        n = len(s)
        words = set()
        
        l = 0
        res = []
        for i, ch in enumerate(s):
            words.add(ch)
            dic[ch] -= 1
            if all(dic[w] == 0 for w in words):
                res.append(i - l + 1)
                l = i + 1
                words = set()
        
        return res