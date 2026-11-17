# https://leetcode.com/problems/contains-duplicate-ii
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        lastIndex = defaultdict(int)
        left = 0
        for right in range(1, len(nums)):
            if lastIndex[nums[right]] != 0:
                left = lastIndex[nums[right]]

            if nums[left] == nums[right] and abs(left-right) <= k:
                return True

            lastIndex[nums[right]] = right
        
        return False