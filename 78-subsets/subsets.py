class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []

        def bt(lst, path, start):
            n = len(lst)

            
            res.append(path[:])

            for i in range(start, n):
                path.append(lst[i])
                
                bt(lst, path, i + 1)
                
                path.pop()

        bt(nums, [], 0)

        return res
