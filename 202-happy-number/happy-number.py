class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while True:
            s = 0
            for i in str(n):
                s += int(i) * int(i)
            if s == 1:
                return True
            if s in nums:
                return False
            nums.add(s)
            n = s