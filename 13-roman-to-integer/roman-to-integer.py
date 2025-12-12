from collections import deque
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        lst = deque(s)
        while lst:
            l = lst.popleft()
            if l == 'I':
                if lst and (lst[0] == 'V' or lst[0] == 'X'):
                    l2 = lst.popleft()
                    res += dic[l2] - dic[l]
                else: res += dic[l]
            elif l == 'X':
                if lst and (lst[0] == 'L' or lst[0] == 'C'):
                    l2 = lst.popleft()
                    res += dic[l2] - dic[l]
                else: res += dic[l]
            elif l == 'C':
                if lst and (lst[0] == 'D' or lst[0] == 'M'):
                    l2 = lst.popleft()
                    res += dic[l2] - dic[l]
                else: res += dic[l]
            else:
                res += dic[l]
        
        return res