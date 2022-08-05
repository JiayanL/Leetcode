# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def findDiameter(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            nonlocal diameter
            leftDiameter = findDiameter(node.left)
            rightDiameter = findDiameter(node.right)
            
            diameter = max(diameter, leftDiameter + rightDiameter)
            
            return 1 + max(leftDiameter, rightDiameter)
        findDiameter(root)
        return diameter