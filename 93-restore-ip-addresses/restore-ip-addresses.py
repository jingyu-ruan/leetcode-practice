class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        def dfs(path, i):
            if i == n:
                if len(path) == 4:
                    res.append('.'.join(path[:]))
                return
            if len(path) > 4:
                return
            
            for j in range(i, min(i + 3, n)):
                clip = s[i:j+1]
                if len(clip) >= 2 and clip[0] == '0':
                    continue
                if 0 <= int(clip) <= 255:
                    dfs(path + [clip], j + 1)
        
        dfs([], 0)
        return res
        


