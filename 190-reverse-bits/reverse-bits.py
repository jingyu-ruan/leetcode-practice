class Solution:
    def reverseBits(self, n: int) -> int:
        binary = format(n, '032b')     # 转为32位二进制
        reversed_binary = binary[::-1] # 字符串反转
        return int(reversed_binary, 2) # 转回十进制