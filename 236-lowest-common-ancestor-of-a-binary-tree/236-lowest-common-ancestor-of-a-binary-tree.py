# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.recursive(root, p, q)
    
    def recursive(self, root, p, q):
        '''
        Insight: Focus on what happens at each root
        '''
        # check for base cases -> either nothing or one of the nodes I'm looking for
        if root is None:
            return None
        
        if root is p or root is q:
            # also this resolves the case where the current node is the LCA
            return root
        
        # check for left and right
        left_search = self.recursive(root.left, p, q)
        right_search = self.recursive(root.right, p, q)
        
        # if I've found both, then the current root is the LCA
        if (left_search and right_search):
            return root
        else:
            return left_search or right_search
        
    def iterative(self, root, p, q):
        pass