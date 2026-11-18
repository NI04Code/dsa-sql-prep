# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        inorderMap = {val: idx for idx, val in enumerate(inorder)}
        self.postIdx = len(postorder) - 1

        def build(left, right):
            if left > right:
                return
            
            val = postorder[self.postIdx]
            self.postIdx -= 1
            root = TreeNode(val)

            mid = inorderMap[val]
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root
        
        return build(0, len(postorder) - 1)
        