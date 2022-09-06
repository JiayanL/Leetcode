# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # shorter version, same idea
        if inorder:
            root_val = preorder.pop(0)
            inorder_index = inorder.index(root_val)
            root = TreeNode(root_val)
            root.left = self.buildTree(preorder, inorder[0:inorder_index])
            root.right = self.buildTree(preorder,inorder[inorder_index + 1:])
            return root
        return None