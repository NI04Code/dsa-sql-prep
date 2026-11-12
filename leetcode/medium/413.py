# https://leetcode.com/problems/arithmetic-slices
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        total = 0
        left = 0
        diff = nums[1] - nums[0]
        for right in range(2, n):
            curr_diff = nums[right] - nums[right - 1]
            if curr_diff == diff:
                total += (right - left + 1) - 2
            else:
                left = right - 1
                diff = curr_diff

        return total
       
                
        