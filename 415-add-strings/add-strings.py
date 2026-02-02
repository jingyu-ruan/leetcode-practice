class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        res = ['0'] * (max(n1, n2) + 1)
        p1, p2 = n1 - 1, n2 - 1
        carry = 0
        for i in range(len(res) - 1, -1, -1):
            total = carry
            if p1 >= 0:
                total += int(num1[p1])
            if p2 >= 0:
                total += int(num2[p2])
            carry = total // 10
            res[i] = str(total % 10)

            p1 -= 1
            p2 -= 1
        start = 0
        while start < len(res) and res[start] == '0':
            start += 1
        if start == len(res):
            return '0'
        return ''.join(res[start:])