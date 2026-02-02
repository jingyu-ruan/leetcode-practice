class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m - 1
        p = m + n - 1
        s2 = n - 1
        
        while l >= 0 and s2 >= 0:
            if nums1[l] >= nums2[s2]:
                nums1[p] = nums1[l]
                l -= 1
                p -= 1
            else:
                nums1[p] = nums2[s2]
                s2 -= 1
                p -= 1
        
        while l >= 0:
            nums1[p] = nums1[l]
            l -= 1
            p -= 1
        
        while s2 >= 0:
            nums1[p] = nums2[s2]
            s2 -= 1
            p -= 1
        
