# https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def dfs(start, sum, path):
            if sum > target:
                return

            if sum == target:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                path.append(num)
                dfs(i, sum+num, path)
                path.pop()

        dfs(0, 0, [])  
        
        return result
        