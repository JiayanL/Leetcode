# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        recursive = False
        if recursive:
            return self.recursive_DFS(root)
        elif not recursive:
            return self.recursive_DFS(root)

    def recursive_DFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.recursive_DFS(root.left), self.recursive_DFS(root.right))
    
    def iterative_BFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque([(root, 1)])
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            if curr.left:
                queue.append((curr.left, depth + 1))
            if curr.right:
                queue.append((curr.right, depth + 1))
        