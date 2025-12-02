class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        maps = {}
        for i, v in enumerate(nums):
            if v in maps and i - maps[v] <= k:
                return True
            maps[v] = i
        
        return False
