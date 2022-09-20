# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        result = []
        leftToRight = True
        queue = collections.deque([root])
        
        while queue:
            currentLevel = collections.deque()
            levelLength = len(queue)
            
            for _ in range(levelLength):
                curr = queue.popleft()
                
                if leftToRight:
                    currentLevel.append(curr.val)
                else:
                    currentLevel.appendleft(curr.val)
                    
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(list(currentLevel))
            leftToRight = not leftToRight
        return result