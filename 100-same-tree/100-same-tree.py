# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # store current nodes as tuples and run bfs
        queue = collections.deque([(p, q)])
        
        # run bfs and check
        while queue:
            tup = queue.popleft()
            p_curr, q_curr = tup[0], tup[1]
            if p_curr and q_curr:
                if p_curr.val != q_curr.val:
                    return False
                queue.append((p_curr.left, q_curr.left))
                queue.append((p_curr.right, q_curr.right))
            elif p_curr or q_curr:
                return False
        return True