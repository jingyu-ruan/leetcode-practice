class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        res = [-1, -1]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                res[0], res[1] = m, m
                cur = m - 1
                while cur >= 0 and nums[cur] == target:
                    res[0] = cur
                    cur -= 1
                nxt = m + 1
                while nxt <= len(nums) - 1 and nums[nxt] == target :
                    res[1] = nxt
                    nxt += 1
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            
        return res