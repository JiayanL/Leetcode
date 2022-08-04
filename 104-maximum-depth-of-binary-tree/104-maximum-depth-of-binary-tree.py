# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        recursive = True
        if recursive:
            return self.recursive_DFS(root)
        elif not recursive:
            return self.recursive_DFS(root)

    def recursive_DFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.recursive_DFS(root.left), self.recursive_DFS(root.right))
    def iterative_BFS(self, root: Optional[TreeNode]) -> int:
        pass