"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        method = "iDFS"
        if method == "iBFS":
            return self.iBFS(node)
        elif method == "iDFS":
            return self.iDFS(node)
        elif method == "rDFS":
            return self.rDFS(node)
    def iBFS(self, node: 'Node') -> 'Node':
        # dictionary to hold all the copies of each node
        copyHolder = {}
        
        if not node:
            return 
        
        # set up general BFS
        queue = deque([node])
        copyHolder[node] = Node(node.val)
        
        while queue:
            currNode = queue.popleft()
            
            for nNode in currNode.neighbors:
                if nNode not in copyHolder: #not visited:
                    queue.append(nNode)
                    copyHolder[nNode] = Node(nNode.val)
                copyHolder[currNode].neighbors.append(copyHolder[nNode])
        
        return copyHolder[node]
            
    def iDFS(self, node: 'Node') -> 'Node':
        visited = {}
        stack = [node]
        if not node:
            return None
        visited[node] = Node(node.val)
        
        while stack:
            curr = stack.pop()
            for nNode in curr.neighbors:
                if nNode not in visited:
                    visited[nNode] = Node(nNode.val)
                    stack.append(nNode)
                visited[curr].neighbors.append(visited[nNode])
        return visited[node]
    
    def rDFS(self, node: 'Node') -> 'Node':
        pass
    

    
            
        