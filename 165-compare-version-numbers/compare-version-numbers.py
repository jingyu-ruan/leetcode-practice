class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n1, n2 = len(v1), len(v2)
        p1, p2 = 0, 0
        while p1 < n1 and p2 < n2:
            if int(v1[p1]) > int(v2[p2]):
                return 1
            if int(v1[p1]) < int(v2[p2]):
                return -1
            p1 += 1
            p2 += 1
        while p1 < n1:
            if int(v1[p1]) != 0:
                return 1
            p1 += 1
        while p2 < n2:
            if int(v2[p2]) != 0:
                return -1
            p2 += 1
        return 0