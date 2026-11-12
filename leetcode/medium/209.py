class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        result = float('inf')
        i = 0; j = 0
        
        sums = 0
        while j < len(nums):
            sums += nums[j]
            while sums >= target:
                result = min(result, j - i + 1)
                sums -= nums[i]
                i += 1
            j += 1
            
        return 0 if result == float('inf') else result