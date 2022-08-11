# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Insight: maintain high low of each branch
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS iterative
        
        stack = [(root, -math.inf, math.inf)]
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if not low < node.val < high:
                return False
            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))
        return True
        