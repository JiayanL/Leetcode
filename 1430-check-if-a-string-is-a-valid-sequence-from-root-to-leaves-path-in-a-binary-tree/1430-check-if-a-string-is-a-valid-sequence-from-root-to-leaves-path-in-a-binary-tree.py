# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        # intuition: run DFS where its true if we hit a leaf
        # false if we don't have the right index
        if not root:
            return False
        return self.findValidSequence(root, arr, 0)
        
    def findValidSequence(self, node, arr, index):
        # empty root
        if not node:
            return False
        
        # check current sequence
        if index >= len(arr) or arr[index] != node.val:
            return False
        
        # check that I'm at a leaf
        if not node.left and not node.right and index == len(arr) - 1:
            return True
        
        # go down both sides
        return self.findValidSequence(node.left, arr, index + 1) or \
    self.findValidSequence(node.right, arr, index + 1)