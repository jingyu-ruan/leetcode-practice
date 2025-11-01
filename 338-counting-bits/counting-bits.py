class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(bin(i).count('1'))  # bin(i) 把数字转成二进制字符串
        return ans