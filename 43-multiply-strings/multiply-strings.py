class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
            1 2 3 i
            4 5 6 j
      0 0 0 0 0 8

        '''
        n1, n2 = len(num1), len(num2)
        n = n1 + n2
        res = [0] * (n1 + n2)
        # p1 = n1 - 1
        # p2 = n2 - 2
        carry = 0
        for j in range(n2 - 1, -1, -1):
            p = n1 + j
            for i in range(n1 - 1, -1, -1):
                total = int(num1[i]) * int(num2[j]) + carry
                carry = total // 10
                res[p] += total % 10
                if res[p] >= 10:
                    val = res[p]
                    res[p] = val % 10
                    carry += val // 10
                p -= 1
            while carry > 0:
                res[p] = carry % 10
                carry //= 10
                p -= 1
        p = 0
        while p < n and res[p] == 0:
            p += 1
        if p == n:
            return '0'
        return ''.join(map(str, res[p:]))



