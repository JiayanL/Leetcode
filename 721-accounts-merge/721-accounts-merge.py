from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph, visited, result = defaultdict(list), set(), []
        
        # create my adjacency list
        for acc in accounts:
            for i in range(2, len(acc)):
                graph[acc[i-1]].append(acc[i])
                graph[acc[i]].append(acc[i-1])
                
        # create my DFS function to find connected components
        def dfs(email, path):
            path.append(email)
            
            for neighbor in graph[email]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, path)
            return path
        
        # loop through all accounts and run DFS
        for acc in accounts:
            if acc[1] not in visited:
                visited.add(acc[1])
                output = dfs(acc[1], [])
                output = [acc[0]] + sorted(output)
                result.append(output)

        return result