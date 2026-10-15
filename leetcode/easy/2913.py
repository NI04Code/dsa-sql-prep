# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        i = 0; j = 1; n = len(nums)
        result = 0
        for i in range(n):
            unique = set()
            for j in range(i, n):
                unique.add(nums[j])
                result += len(unique)**2
        
        return result
        