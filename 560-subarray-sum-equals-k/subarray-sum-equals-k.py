from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        cur = 0
        res = 0
        for i in nums:
            cur += i
            # cur - past = k
            # past = cur - k
            if cur - k in dic:
                res += dic[cur - k]
            dic[cur] += 1
        
        return res