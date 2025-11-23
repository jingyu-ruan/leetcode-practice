from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in nums:
                dic[i] += 1
        # res = 0
        for j in dic:
            if dic[j] == 1:
                return j
        
        # return res