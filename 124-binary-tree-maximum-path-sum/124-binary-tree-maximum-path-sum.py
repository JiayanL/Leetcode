# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf
        
        def findMaxSum(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0
            
            max_sum_left = findMaxSum(node.left)
            max_sum_right = findMaxSum(node.right)
            
            # case 1: pivot point
            current_sum = max_sum_left + max_sum_right + node.val
            max_sum = max(max_sum, current_sum)
            
            # case 2: part of branch
            branch_sum = max(max_sum_left, max_sum_right) + node.val
            # don't return negative numbers
            if branch_sum < 0:
                return 0
            return branch_sum
        
        findMaxSum(root)
        return max_sum