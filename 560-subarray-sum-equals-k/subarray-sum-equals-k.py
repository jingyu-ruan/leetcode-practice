from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        res = 0
        cur = 0
        for i in nums:
            cur += i
            if cur - k in dic:
                res += dic[cur - k]
            
            dic[cur] += 1
        
        return res
