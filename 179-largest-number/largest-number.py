class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))
        strs.sort(key=lambda x: x* 10, reverse = True)
        return ''.join(strs) if ''.join(strs)[0] != '0' else '0'
