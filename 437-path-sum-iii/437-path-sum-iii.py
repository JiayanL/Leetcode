# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # O(n) -> prefix sum    
        prefix_sum = {}
        return self.dfs_findPathSum(root, targetSum, prefix_sum, 0)
    
    def dfs_findPathSum(self, root, targetSum, prefix_sum, current_sum):
        if not root:
            return 0
        
        pathCount = 0
        current_sum += root.val
        # case 1: I have the sum
        if current_sum == targetSum:
            pathCount += 1
            
        # case 2: current_sum - targetSum exists along this path]
        pathCount += prefix_sum.get(current_sum - targetSum, 0)
        
        # add prefix to array
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        pathCount += self.dfs_findPathSum(root.left, targetSum, prefix_sum, current_sum) + \
        self.dfs_findPathSum(root.right, targetSum, prefix_sum, current_sum)
        
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 1) - 1
        
        return pathCount