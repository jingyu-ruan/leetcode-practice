class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. 始终保持 nums1 是较短的那个
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = total_left - i

            # 2. 关键修改：处理边界情况，使用无穷大/小
            # 如果 i == 0，说明 nums1 左边没元素，设为 -inf
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            # 如果 i == m，说明 nums1 右边没元素，设为 inf
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            # 3. 交叉判断
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 找到啦！
                if (m + n) % 2 == 0:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
                else:
                    return max(nums1_left_max, nums2_left_max)
            
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1