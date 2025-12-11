
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1        # nums1 的有效部分末尾
        j = n - 1        # nums2 的末尾
        k = m + n - 1    # nums1 的总末尾

        # 从后往前填
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # nums2 可能还没放完（nums1 没必要处理，因为剩下来的已经在前面）
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        
        