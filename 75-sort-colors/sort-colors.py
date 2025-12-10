from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_dic = Counter(nums)
        for i in range(len(nums)):
            if num_dic[0] > 0:
                num_dic[0] -= 1
                nums[i] = 0
            elif num_dic[1] > 0:
                num_dic[1] -= 1
                nums[i] = 1
            else:
                nums[i] = 2