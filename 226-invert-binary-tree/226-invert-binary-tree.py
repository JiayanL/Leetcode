# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs iterative
        return self.bfsIterative(root)
        # dfs iterative
        # dfs recursive
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