# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n):
            left = i+1; right = n-1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]

                if abs(target - threeSum) < abs(target - result):
                    result = threeSum
                
                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    return result

        return result