# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        queue = deque([root])
        result = []
        while queue:
            layerLength = len(queue)
            layer = []
            for i in range(layerLength):
                currNode = queue.popleft()
                layer.append(currNode.val)
                # append children
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
                
            result.append(layer)
        return result
                
            