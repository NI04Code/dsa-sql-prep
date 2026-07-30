# https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_val = self.checkTree(p)
        q_val = self.checkTree(q)

        a, b = len(p_val), len(q_val)
        if a != b:
            return False
        
      
        for i in range(a):
            if p_val[i] != q_val[i]:
                return False

        return True


    
    def checkTree(self, root: Optional[TreeNode]) -> List:
        val = []

        if root == None:
            val.append(None)
            return val

        queue = []
        queue.append(root)

        val.append(root.val)
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left != None:
                if node.left not in visited:
                    queue.append(node.left)

                    val.append(node.left.val)
            else:
                val.append(None)

            if node.right != None:
                if node.right not in visited:
                    queue.append(node.right)
                    visited.append(node.right)
                    val.append(node.right.val)
            else:
                val.append(None)
        
        return val

                


        