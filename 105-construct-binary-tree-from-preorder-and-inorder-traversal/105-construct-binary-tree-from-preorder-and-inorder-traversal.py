# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def arrayToTree(left_index, right_index):
            # left and right index tell us the part of the subtree we're working with
            nonlocal preorder_index
            
            # check if this is still valid
            if left_index > right_index:
                return None
            
            current_root = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(current_root)
            # create a node with my current root
            
            # add the left and right for my current root
            root.left = arrayToTree(left_index, inorder_root_index[current_root] - 1)
            root.right = arrayToTree(inorder_root_index[current_root] + 1, right_index)
            
            return root
        # keep track of the root
        preorder_index = 0
        inorder_root_index = {}
        
        # keep track of where each root is in the inorder list
        for i in range(len(inorder)):
            inorder_root_index[inorder[i]] = i
        
        return arrayToTree(0, len(preorder) - 1)
        