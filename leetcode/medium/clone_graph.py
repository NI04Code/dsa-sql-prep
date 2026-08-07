# https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque([node])
        visited = [node]

        new_nodes = [None] * 100
        new_nodes[0] = Node(node.val)
        while queue:
            curr = queue.popleft()
            p = new_nodes[curr.val - 1]
            for n in curr.neighbors:
                if n not in visited:
                    queue.append(n)
                    visited.append(n)
                    
                    if not new_nodes[n.val-1]:
                        new_nodes[n.val-1] = Node(n.val)

                    
                if not p.neighbors:
                    p.neighbors = []
                
                p.neighbors.append(new_nodes[n.val-1])

        return new_nodes[0]