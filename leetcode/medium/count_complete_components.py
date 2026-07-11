# https://leetcode.com/problems/count-the-number-of-complete-components/
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                v = 0
                e_sum = 0
                
                queue = [i]
                visited[i] = True
                
                while queue:
                    curr = queue.pop(0)
                    v += 1
                    e_sum += len(adj[curr])
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
            
                if e_sum == v * (v - 1):
                    count += 1
        
        return count


