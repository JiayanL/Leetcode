class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #edge case
        if n <= 2:
            return [i for i in range(n)]
        # create an adjacency list
        neighbors = [set() for _ in range(n)]
        for edge in edges:
            neighbors[edge[0]].add(edge[1])
            neighbors[edge[1]].add(edge[0])
        
        # find all leaves
        leaves = []
        for node in range(n):
            if len(neighbors[node]) == 1:
                leaves.append(node)
                
        # while I haven't found the centroids, prune the leaves
        nodes_remaining = n
        while nodes_remaining > 2:
            leaf_count = len(leaves)
            nodes_remaining -= len(leaves)
        
            new_leaves = []
            # remove all leaves
            while leaves:
                current_leaf = leaves.pop()
                leaf_neighbor = neighbors[current_leaf].pop()
                
                neighbors[leaf_neighbor].remove(current_leaf)
                if len(neighbors[leaf_neighbor]) == 1:
                    new_leaves.append(leaf_neighbor)
            leaves = new_leaves
            
            # add new leaves
        return leaves