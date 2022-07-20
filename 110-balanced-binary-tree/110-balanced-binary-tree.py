# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   # bottom up solution: check if children are balanced, then use their heights to check if parent is balanced
    
    def balancedHelper(self, root:Optional[TreeNode]):
        if not root:
            return True, 0
        
        leftisBalanced, leftHeight = self.balancedHelper(root.left)
        if not leftisBalanced:
            return False, 0
        
        rightisBalanced, rightHeight = self.balancedHelper(root.right)
        if not rightisBalanced:
            return False, 0
        
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balancedHelper(root)[0]
