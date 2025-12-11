class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        rep = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write] = nums[i]
                rep = 1
                write += 1
            else:
                if rep == 1:
                    nums[write] = nums[i]
                    rep = 2
                    write += 1
        
        return write
