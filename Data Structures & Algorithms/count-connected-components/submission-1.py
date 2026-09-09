class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list from edges
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Visit list
        visit = [False] * n

        # DFS nodes + neighbors
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        # Count components
        res = 0
        for node in range(n):
            # Visit node if not already
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        
        return res