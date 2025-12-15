class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(lst, remains):
            if len(lst) == n:
                    res.append(lst)
                    return

            for i in remains:
                new_remains = [x for x in remains if x != i]
                new_lst = lst + [i]
                dfs(new_lst, new_remains)
        
        dfs([], nums)
        return res