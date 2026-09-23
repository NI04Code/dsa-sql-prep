# https://leetcode.com/problems/first-missing-positive
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        found = [0 for i in range(len(nums)+1)]
        for num in nums:
            if num > 0 and num <= len(nums):
                found[num] = 1
        
        for i in range(1, len(found)):
            if found[i] == 0:
                return i
        

        return len(nums)+1