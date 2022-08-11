# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# top down
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return (self.isValid(root))
        
    def isValid(self, node, low=-math.inf, high=math.inf) -> bool:
        # if I've reached the end, it's balanced
        if not node:
            return True
        
        # check that my node is between the low and highs for this part of the branch
        if not low < node.val < high:
            return False
        
        # adjust limits - when I move left, the new high is current val
        # when I move right, the new low, is current low
        return (self.isValid(node.left, low, node.val) and self.isValid(node.right, node.val, high))