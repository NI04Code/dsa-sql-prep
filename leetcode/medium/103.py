# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = []
        queue.append(root)

        result = []
        count = 0
        while len(queue) > 0:
            level = len(queue)
            curr = []
            
            for i in range(level):
                node = queue.pop(0)
            
                if count % 2 == 0:
                    curr.append(node.val)
                else:
                    curr.insert(0, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(curr)
            count += 1
            
        return result

            