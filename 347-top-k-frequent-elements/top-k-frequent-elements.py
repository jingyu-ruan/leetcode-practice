from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        cnt = Counter(nums)
        cnt_lst = list(cnt.items())
        cnt_lst.sort(key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(cnt_lst[i][0])

        return res