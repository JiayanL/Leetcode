# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs iterative
        # return self.bfsIterative(root)
        # dfs iterative
        # return self.dfsIterative(root)
        # dfs recursive
        return self.dfsRecursive(root)
    
    def bfsIterative(self, root):
        # create queue
        queue = collections.deque([root])
        # bfs swap -> checking that current node is valid
        while queue:
            node = queue.popleft()
            if node:
                # I have to do this on the same line so I don't lose it
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
    
    def dfsIterative(self, root):
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
    
    def dfsRecursive(self, root):
        if root:
            root.left, root.right = self.dfsRecursive(root.right), self.dfsRecursive(root.left)
        return root