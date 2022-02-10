# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check that root is valid
        if not root:
            return None
        # initialize queue for bfs
        bfs_queue = collections.deque([root])
        # bfs on Tree -> swap children and then add children to queue
        while bfs_queue:
            curr_node = bfs_queue.popleft()
            # swap children
            temp = curr_node.left
            curr_node.left = curr_node.right
            curr_node.right = temp
            
            # add children to queue
            if curr_node.left:
                bfs_queue.append(curr_node.left)
            if curr_node.right:
                bfs_queue.append(curr_node.right)
        return root