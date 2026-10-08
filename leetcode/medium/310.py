
# https://leetcode.com/problems/minimum-height-trees

from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        leaves = deque([i for i in range(n) if degree[i] == 1])
        remainingNodes = n
        while remainingNodes > 2:
            countLeaf = len(leaves)
            remainingNodes -= countLeaf

            for i in range(countLeaf):
                leaf = leaves.popleft()
                for nbrNode in adj[leaf]:
                    degree[nbrNode] -= 1
                    if degree[nbrNode] == 1:
                        leaves.append(nbrNode)
        
        return list(leaves)