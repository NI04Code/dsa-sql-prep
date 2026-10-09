# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricSlow(self, root: TreeNode | None) -> bool:
        if root.left ==  None and root.right == None:
            return True

        def dfs(root, lst, reverse):
            if root == None:
                lst.append(-101)
                return
            
            lst.append(root.val)
            
            if reverse:
                dfs(root.right, lst, reverse)
                dfs(root.left, lst, reverse)
            else:
                dfs(root.left, lst, reverse)
                dfs(root.right, lst, reverse)
        
        leftList = []
        rightList = []

        dfs(root.left, leftList, False)
        dfs(root.right, rightList, True)

        for i in range(len(leftList)):
            if leftList[i] != rightList[i]:
                return False

        return True

    def isSymmetricFast(self, root: TreeNode | None) -> bool:
        if root.left ==  None and root.right == None:
            return True

        def isMirror(l, r):
            if not l and not r:
                return True

            if not l or not r:
                return False
            
            return (l.val == r.val) and \
                   isMirror(l.left, r.right) and \
                   isMirror(l.right, r.left)

        return isMirror(root.left, root.right)
        
        