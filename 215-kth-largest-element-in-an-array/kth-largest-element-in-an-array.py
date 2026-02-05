class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            k = arr[len(arr) // 2]
            left = [i for i in arr if i > k]
            equal = [i for i in arr if i == k]
            right = [i for i in arr if i < k]

            return quick_sort(left) + equal + quick_sort(right)
        
        a = quick_sort(nums)
        return a[k-1]