# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for num in numSet:
            if num - 1 not in numSet:
                curr = num
                streak = 1

                while curr + 1 in numSet:
                    curr = curr + 1
                    streak += 1
                
                maxLen = max(maxLen, streak)
            
        return maxLen
        