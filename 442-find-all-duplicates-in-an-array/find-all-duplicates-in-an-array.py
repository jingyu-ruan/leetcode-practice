class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numset = set()
        res = []
        for num in nums:
            if num in numset:
                res.append(num)
            numset.add(num)
        return res