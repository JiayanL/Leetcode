# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBranchBalanced(root)[0]
        
    def isBranchBalanced(self, root: Optional[TreeNode]):
        if not root:
            return True, 0
    
        balanced = True
        left_balanced, left_height = self.isBranchBalanced(root.left)

        right_balanced, right_height = self.isBranchBalanced(root.right)
        
        if not left_balanced or not right_balanced:
            balanced = False
        if abs(right_height - left_height) >= 2:
            balanced = False
        
        return balanced, 1 + max(left_height, right_height)