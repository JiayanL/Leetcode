# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # O(n^2) -> DFS, check targetSum
        return self.dfs_findPath(root, targetSum, [])
    
    def dfs_findPath(self, node, targetSum, path):
        if not node:
            return 0
        
        path.append(node.val)
        current_path_sum = 0
        pathCount = 0
        
        for i in range(len(path) - 1, -1, -1):
            curr = path[i]
            current_path_sum += curr
            if current_path_sum == targetSum:
                pathCount += 1
            
        pathCount += self.dfs_findPath(node.left, targetSum, path)
        pathCount += self.dfs_findPath(node.right, targetSum, path)
        
        path.pop()
        return pathCount