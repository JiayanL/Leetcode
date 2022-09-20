"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        # level traversal
        queue = collections.deque([root])
        
        while queue:
            levelLength = len(queue)
            previousNode = None
            
            for _ in range(levelLength):
                curr = queue.popleft()
                if previousNode:
                    previousNode.next = curr
                previousNode = curr
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root