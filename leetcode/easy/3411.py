# https://leetcode.com/problems/maximum-subarray-with-equal-products
import math

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        left = 0
        maxLen = 0
        for right in range(1, len(nums)+1):
            subarr = nums[left:right]
            prod = math.prod(subarr); gcd = math.gcd(*subarr); lcm = math.lcm(*subarr)

            while prod != gcd * lcm and right - left > 1:
                left += 1
                subarr = nums[left:right]
                prod = math.prod(subarr); gcd = math.gcd(*subarr); lcm = math.lcm(*subarr)
            
            if prod == gcd * lcm:
                maxLen = max(maxLen, right - left)
        
        return maxLen