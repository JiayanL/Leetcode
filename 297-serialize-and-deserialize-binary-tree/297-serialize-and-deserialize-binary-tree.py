# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        serialized_tree = []
        queue = collections.deque([root])
        while queue:
            curr = queue.popleft()
            
            if curr == "null":
                serialized_tree.append("null")
                continue
            else:
                serialized_tree.append(str(curr.val))
            
            # append left and right children
            if curr.left:
                queue.append(curr.left)
            else:
                queue.append("null")
            
            if curr.right:
                queue.append(curr.right)
            else:
                queue.append("null")
        
        serialized_string = ','.join(serialized_tree)
        return serialized_string
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        
        serialized_array = collections.deque(data.split(','))
        
        # construct with bfs
        root = TreeNode(serialized_array.popleft())
        
        queue = collections.deque([root])
        
        while serialized_array:
            curr_node = queue.popleft()
            left_val = serialized_array.popleft()
            right_val = serialized_array.popleft()
            
            if left_val != "null":
                curr_node.left = TreeNode(left_val)
                queue.append(curr_node.left)
            if right_val != "null":
                curr_node.right = TreeNode(right_val)
                queue.append(curr_node.right)
                
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))