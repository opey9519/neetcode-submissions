class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Set hashmap for each course has no prereqs
        preMap = {i: [] for i in range(numCourses)}

        # Set the prereqs for each course from given array
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # Stores all courses along current DFS path
        visiting = set()

        def dfs(crs):
            # Cycle detected
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)
            # Loop through all prereqs
            for pre in preMap[crs]:
                # If cycle
                if not dfs(pre):
                    return False
                
            # No longer visiting
            visiting.remove(crs)
            preMap[crs] = [] # No repeated work
            return True

        # Check if all courses can be completed, even disconnected graphs
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True