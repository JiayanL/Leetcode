# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def findDeepestRoot(node: Optional[TreeNode]):
            if not node:
                return 0
            nonlocal diameter
            left_max = findDeepestRoot(node.left)
            right_max = findDeepestRoot(node.right)
            diameter = max(diameter, left_max + right_max)

            return 1 + max(left_max, right_max)
        
        findDeepestRoot(root)
        return diameter
