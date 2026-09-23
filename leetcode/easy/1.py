# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    two_sum.append(i)
                    two_sum.append(j)
                    break
            
            if len(two_sum) == 2:
                break
        
        return two_sum
        