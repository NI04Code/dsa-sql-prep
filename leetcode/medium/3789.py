# https://leetcode.com/problems/minimum-cost-to-acquire-required-items

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        minCost = 0
        if costBoth >= cost1 + cost2:
            minCost += (cost1 * need1 + cost2 * need2)
        else:
            minCost += costBoth * min(need1, need2)
            
            if need1 > need2:
                minCost += min(costBoth, cost1) * (need1 - need2)
            elif need2 > need1:
                minCost += min(costBoth, cost2) * (need2 - need1)
        
        return minCost

