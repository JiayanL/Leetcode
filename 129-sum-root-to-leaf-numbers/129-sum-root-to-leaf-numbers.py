# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs_sum(root, 0)
    def dfs_sum(self, node, current_sum) -> int:
        if not node:
            return 0
        
        # add to the sum
        current_sum = current_sum * 10 + node.val

        # check that I've reached a leaf
        if not node.left and not node.right:
            return current_sum
        
        return self.dfs_sum(node.left, current_sum) + self.dfs_sum(node.right, current_sum)