class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        '''
        1 2 3 
          1 1
        
        3 2 1
        1 1
        '''
        rev1 = num1[::-1]
        rev2 = num2[::-1]
        n1, n2 = len(num1), len(num2)
        # p = 0
        carry = 0
        res = ''
        for i in range(max(n1, n2)):
            total = carry
            if i < n1:
                total += int(rev1[i])
            if i < n2:
                total += int(rev2[i])
            res += str(total % 10)
            carry = total // 10
        if carry > 0:
            res += str(carry)
        return res[::-1]
