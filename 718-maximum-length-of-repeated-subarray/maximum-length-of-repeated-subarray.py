class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''
          # 1 2 3 2 1
        # 0 0 0 0 0 0
        3 0 0 0 1 1 1
        2 0 0 1 1 2 2
        1 0 1 1 1 2 3
        4 0
        7 0

          # 0 1 1 1 1
        # 0 0 0 0 0 0
        1 0 0 1 1 1 1
        0 0 1 1 1 1 1
        1 0 1 2 2 2 2
        0 0 1 2 2 2 2
        1 0 1 2 3
        '''
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        res = 0
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if nums1[j-1] == nums2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
        
        return res