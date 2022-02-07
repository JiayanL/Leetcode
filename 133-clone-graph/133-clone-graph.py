"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        ## ✅ run iterative bfs
        return self.iterativebfs(node)
        ## ✅ run iterative dfs
        return self.iterativedfs(node)
        ## ✅ run recursive dfs
        return self.recursivedfs(node)
    
    def iterativebfs(self, node: 'Node') -> 'Node':
        # check that node is valid
        if not node:
            return node
        # initialize variables 
        # dictionary contains deep copy of each node
        deep_copy = {node: Node(node.val)}
        
        # use a queue for bfs
        queue = collections.deque([node])
        
        # breadth first search
        while queue:
            curr_node = queue.popleft()
            # check if seen
            for neighbor in curr_node.neighbors:
                if neighbor not in deep_copy:
                    deep_copy[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                deep_copy[curr_node].neighbors.append(deep_copy[neighbor])
        return deep_copy[node]
        
    def iterativedfs(self, node: 'Node') -> 'Node':
        # check that node is valid
        if not node:
            return node
        # initialize dictionary and stack(dfs)
        deep_copy = {node: Node(node.val)}
        stack = [node]
        
        # do dfs
        while stack:
            curr_node = stack.pop()
            for neighbor in curr_node.neighbors:
                if neighbor not in deep_copy:
                    stack.append(neighbor)
                    deep_copy[neighbor] = Node(neighbor.val)
                deep_copy[curr_node].neighbors.append(deep_copy[neighbor])
        # return node
        return deep_copy[node]
    
    def recursivedfs(self, node: 'Node') -> 'Node':
        def dfs(node: 'Node'):
            if not node:
                return None
            # return node if visited
            elif node in deep_copy:
                return deep_copy[node]
            # visit node
            deep_copy[node] = Node(node.val)
            # visit neighbors
            for neighbor in node.neighbors:
                print(neighbor)
                deep_copy[node].neighbors.append(dfs(neighbor))
            return deep_copy[node]
        # dictionary contains deep copy of each node
        deep_copy = {}
        return dfs(node)
    
            
        