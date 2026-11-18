# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorderMap = {val: idx for idx, val in enumerate(inorder)}
        self.preIdx = 0

        def build(left, right):
            if left > right:
                return
            
            val = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(val)

            mid = inorderMap[val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(preorder) - 1)

        