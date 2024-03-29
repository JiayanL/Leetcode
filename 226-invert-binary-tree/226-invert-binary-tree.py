# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        solution = "bfs"
        if solution == "dfs":
            return self.dfs(root)
        if solution == "bfs":
            return self.bfs(root)
        if solution == "recursive":
            return self.recursive(root)
        
    def dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        stack = [root]
        
        while stack:
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return root
    
    def bfs(Self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        queue = collections.deque([root])
        
        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
        return root
    
    def recursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
            