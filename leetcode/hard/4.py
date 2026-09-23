# https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = sorted(nums1 + nums2)
        arr_len = len(new_arr)
        if arr_len % 2 == 0:
            median = (new_arr[arr_len // 2] + new_arr[(arr_len // 2) - 1]) / 2
        else:
            median = new_arr[arr_len // 2]

        return median