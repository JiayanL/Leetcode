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
            # log the entire level
            currLayer = []
            nextLayer = []
            while queue:
                currNode = queue.popleft()
                
                # append children
                if currNode.left:
                    nextLayer.append(currNode.left)
                if currNode.right:
                    nextLayer.append(currNode.right)
                
                currLayer.append(currNode.val)
            result.append(currLayer)
            for node in nextLayer:
                queue.append(node)
        return result
                
            