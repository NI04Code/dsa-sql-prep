# https://leetcode.com/problems/combination-sum-ii
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        sortedCand = sorted(candidates)
        result = []
        def dfs(start, sum, path):
            if sum > target:
                return
            
            if sum == target:
                result.append(path.copy())
                return
            
            for i in range(start, len(sortedCand)):
                if i > start and sortedCand[i] == sortedCand[i - 1]:
                    continue

                num = sortedCand[i]
                path.append(num)
                dfs(i+1, sum+num, path)
                path.pop()
        
        dfs(0, 0, [])
        return result