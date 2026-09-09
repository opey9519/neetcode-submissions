class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If more edges than nodes -> false
        if len(edges) > n - 1:
            return False

        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visiting = set()

        def dfs(node, par):
            # Base Case: Node is already visited -> Cycle
            if node in visiting:
                return False
            
            visiting.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False

            return True
        
        return dfs(0, -1) and len(visiting) == n