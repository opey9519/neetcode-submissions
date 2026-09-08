"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hashmap to store deep copy
        hmap = {}

        def dfs(node):
            # Base Case: Node already visited 
            if node in hmap:
                return hmap[node]
            
            # Clone and store reference
            copy = Node(node.val)
            hmap[node] = copy

            # Create all neighbors
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        
        return dfs(node) if node else None

        