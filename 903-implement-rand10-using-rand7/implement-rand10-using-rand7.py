# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # 1. 构造 1-49 的均匀分布
            # (row - 1) * 7 + col
            # 范围: (0~6) * 7 + (1~7) = 1 ~ 49
            num = (rand7() - 1) * 7 + rand7()
            
            # 2. 拒绝采样：只接受 1-40
            if num <= 40:
                # 3. 映射回 1-10
                return (num - 1) % 10 + 1