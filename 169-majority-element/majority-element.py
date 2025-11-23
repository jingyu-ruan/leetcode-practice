from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        candi = 0

        for i in nums:
            if cnt == 0:
                candi = i
            
            if i == candi:
                cnt += 1
            else:
                cnt -= 1
        
        return candi