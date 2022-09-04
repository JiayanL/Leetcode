# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # run layer by layer bfs
        result = []
        layer = collections.deque([root])
        
        while layer:
            result.append(layer[-1].val)
            for i in range(len(layer)):
                curr = layer.popleft()
                if curr.left:
                    layer.append(curr.left)
                if curr.right:
                    layer.append(curr.right)
        return result
        